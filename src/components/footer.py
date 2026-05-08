import streamlit as st

def footer_home():
    st.markdown(f"""
                 
      <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center" >
        <p style="color:white;"> Created with ❤️ by Deekshitha Varma </p>
      </div>
      
     """,unsafe_allow_html=True)
    

def footer_dashboard():
    st.markdown(f"""
                 
      <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center" >
        <p style="color:black;"> Created with ❤️ by Deekshitha Varma </p>
      </div>
      
     """,unsafe_allow_html=True)
