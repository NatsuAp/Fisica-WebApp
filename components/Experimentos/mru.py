import streamlit as st
from Utils import pageManager
def deployMRU():
    st.title("Empieza el experimento...")
    st.image("resources\loading.gif")
    if st.button("Regresar"):
        pageManager.page = "homepage"
        st.rerun()