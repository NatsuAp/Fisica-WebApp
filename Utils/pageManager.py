import streamlit as st
if "page" not in st.session_state:
    st.session_state.page = "login"
page = st.session_state.page
