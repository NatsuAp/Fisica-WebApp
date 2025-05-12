import streamlit as st
from Utils import pageManager

    
def deployHomePage():
    if "friccion" not in st.session_state:
        st.session_state.friccion = False
        
    with st.container(height=None, border=None, key=None):
        st.title("Escoge tu experimento")
        st.header("Movimiento Rectilineo Uniforme (MRU)")
        st.image("resources\MRUIMG.png")
        if st.button("Iniciar", key="mru"):
            st.session_state.friccion = True
            st.rerun()
    if st.session_state.friccion:
        col1, col2= st.columns(2)
        with col1:
            if st.button("Con friccion"):
                pageManager.page = "mru"
                st.rerun()
        with col2:
            if st.button("Sin friccion"):
                pageManager.page = "mru"
                st.rerun()   
    st.header("Caida Libre")
    st.image("resources\CLIMG.png")
    if st.button("Iniciar", key="cl"):
            pageManager.page = "cl"
            st.rerun()
        
            
            



    