import streamlit as st
if not st.session_state.get("login"):
    st.error("You must Login")
    st.page_link(label="Go to Login", page="home.py")
else:    
    st.subheader("This is Settings page")

    st.page_link( label="products",page="pages/products.py",icon="⌨️")