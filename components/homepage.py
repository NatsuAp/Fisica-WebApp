import streamlit as st
from Utils import pageManager

    
def deployHomePage():
    
    
    with st.container():
        st.title("Escoge tu experimento")
        st.header("Movimiento Rectilineo Uniforme (MRU)")
        st.image("resources/MRUIMG.png")
        if st.button("Iniciar", key="mru"):
            pageManager.st.session_state.page = "mru"
            st.rerun()
    st.header("Movimiento Rectilineo Acelerado (MRA)")
    st.image("resources/MRA.png")
    if st.button("Iniciar", key="mra"):
        st.write("todavia no hay nada pai")
        
        
    st.header("Caida Libre")
    st.image("resources/CLIMG.png")
    if st.button("Iniciar", key="cl"):
            pageManager.st.session_state.page = "cl"
            st.rerun()
    
    
        
            
            



    