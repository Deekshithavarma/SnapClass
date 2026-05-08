import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
import cv2

from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())
    facerec = dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())
    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 2)

    encoding = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape)
        encoding.append(np.array(face_descriptor))

    print("Faces detected:", len(faces))
    print("Encodings length:", len(encoding))

    return encoding

@st.cache_resource
def get_trained_model():
    X=[]
    Y=[]
    
    student_db=get_all_students()
    
    if not student_db:
        return None
    
    for student in student_db:
        embeddings=student.get('face_embedding')
        # print("get_trained_model",embeddings)
        if embeddings:
            X.append(np.array(embeddings))
            Y.append(student.get('student_id'))
    

    if len(X)==0:
        return 0
          
    clf=SVC(kernel='linear', probability=True,class_weight='balanced')
   
    try:
        clf.fit(X,Y)
    except ValueError:
        pass
   
    return {"clf":clf,"X":X,"Y":Y}


def train_classifier():
    st.cache_resource.clear()
    model_data=get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings=get_face_embeddings(class_image_np)
    # print("Encodings obtained:", encodings[0])

    if not encodings:
     return {}, [], 0

    detected_students={}
    
    model_data=get_trained_model()
    if not model_data:
        return detected_students, [], 0 if not encodings else len(encodings)
    
    clf=model_data['clf']
    X_train=model_data['X']
    y_train=model_data['Y']
    # print("y_train:", y_train)

    all_students=sorted(list(set(y_train)))
    # print("All students in database:", all_students)
    
    for encoding in encodings:
        if len(all_students)>1:
            predicted_id=int(clf.predict([encoding])[0])
        else:
            predicted_id=int(all_students[0])
      
        student_embedding=X_train[y_train.index(predicted_id)]
        
        best_match_score=np.linalg.norm(student_embedding-encoding)
        dist = np.linalg.norm(np.array(student_embedding) - np.array(encoding))
        

        resemblance_threshold=0.6

        if best_match_score<=resemblance_threshold:   
            detected_students[predicted_id]=True

    return detected_students,all_students,len(encodings)       

           

   