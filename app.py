# import streamlit as st
# from src.screens.home_screen import home_screen
# from src.screens.teacher_screen import teacher_screen
# from src.screens.student_screen import student_screen
# from src.components.dialog_auto_enroll import auto_enroll_dialog

# def main():
#     st.set_page_config(page_title="SnapClass - Making Attendance faster using AI", page_icon="https://i.ibb.co/YTYGn5qV/logo.png", layout="wide")

#     if 'login_type' not in st.session_state:
#         st.session_state['login_type'] = None

#     match st.session_state['login_type']:
#         case 'teacher':
#             teacher_screen()
        
#         case 'student':
#             student_screen()
        
#         case None:
#             home_screen()

#     join_code = st.query_params.get('join-code')
#     if join_code:
#         if st.session_state.login_type != 'student':
#             st.session_state.login_type ='student'
#             st.rerun()

#         if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
#             auto_enroll_dialog(join_code)    

# main()    

import streamlit as st
import traceback

st.set_page_config(page_title="Debug Mode")

st.title("SnapClass Import Debugger")

try:
    from src.screens.home_screen import home_screen
    st.success("home_screen imported")
except Exception:
    st.error("home_screen FAILED")
    st.code(traceback.format_exc())

try:
    from src.screens.teacher_screen import teacher_screen
    st.success("teacher_screen imported")
except Exception:
    st.error("teacher_screen FAILED")
    st.code(traceback.format_exc())

try:
    from src.screens.student_screen import student_screen
    st.success("student_screen imported")
except Exception:
    st.error("student_screen FAILED")
    st.code(traceback.format_exc())

try:
    from src.components.dialog_auto_enroll import auto_enroll_dialog
    st.success("auto_enroll_dialog imported")
except Exception:
    st.error("auto_enroll_dialog FAILED")
    st.code(traceback.format_exc())