import streamlit as st
import requests

api_url = "http://localhost:8000"
if "login" not in st.session_state:
    st.session_state.login = False
    st.session_state.user = None
    st.session_state.token = None
if not st.session_state.login:    
    username=st.text_input("Enter Username")
    password=st.text_input("Enter Password")
    if st.button("Login"):
        user = requests.post("http://localhost:8000/login", json={"email": username, "password": password})
        if user.status_code == 200:
            st.session_state.login = True
            st.session_state.user = user.json()["name"]
            st.session_state.token = user.json()["token"]
            st.success(user.json()["message"])
            st.rerun()
        else:
            st.error(user.json()["message"])
else: 
    st.subheader(f"Welcome {st.session_state.user}")  

    

