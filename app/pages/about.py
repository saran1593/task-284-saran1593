import streamlit as st
import requests
if not st.session_state.get("login"):
    st.error("You must Login")
    st.page_link(label="Go to Login", page="home.py")
else:    
    st.subheader(f"Welcome {st.session_state.user}")
    users = requests.get("http://localhost:8000/get-students", headers={"Authorization": f"Bearer {st.session_state.token}"})
    st.write(users.json())
    st.page_link( label="products",page="pages/products.py",icon="⌨️")