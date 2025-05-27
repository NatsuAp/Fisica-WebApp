import streamlit as st
from Utils import pageManager

    
def deployHomePage():
    
    print(st.session_state.nombre_Profesor)  
    with st.container(height=None, border=None, key=None):
        st.title("Escoge tu experimento")
        st.header("Movimiento Rectilineo Uniforme (MRU)")
        st.image("resources\MRUIMG.png")
        if st.button("Iniciar", key="mru"):
            pageManager.page = "mru"
            st.rerun()
    st.header("Movimiento Rectilineo Acelerado (MRA)")
    st.image("resources\MRA.png")
    if st.button("Iniciar", key="mra"):
        st.write("todavia no hay nada pai")
        
        
    st.header("Caida Libre")
    st.image("resources\CLIMG.png")
    if st.button("Iniciar", key="cl"):
            pageManager.page = "cl"
            st.rerun()
    
    
        
            
            



    