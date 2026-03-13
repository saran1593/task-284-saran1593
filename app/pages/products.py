import streamlit as st
if st.session_state.get("login"):
    st.subheader("This is Products page")
else:
    st.error("You must Login")
    st.page_link(label="Go to Login", page="home.py")