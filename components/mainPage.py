import threading
import time
import streamlit as st
from arduino.connection import checkConnection, asyncCall
import Utils.pageManager as pageManager

   
def deployMainPage():
    
    if "clicked" not in st.session_state:
        st.session_state.clicked = False
    if "disabled" not in st.session_state:
        st.session_state.disabled = False    
    if "connection" not in st.session_state:
        st.session_state.connection = False    
    if "expButton" not in st.session_state:
        st.session_state.expButton = True
    if "success" not in st.session_state:
        st.session_state.success = False 
    if "failure" not in st.session_state:
        st.session_state.failure = False   
    

    st.title("***Conecta el arduino***")
    
    if st.button('Iniciar conexión', key="conexion", disabled=st.session_state.disabled):
        st.session_state.clicked = True
        st.rerun()
    if st.button("Iniciar experimento", disabled=st.session_state.expButton):
               pageManager.page="homepage"
               st.rerun()
    if st.session_state.clicked:
        with st.spinner("Estableciendo conexión", show_time=True):
            arduino = checkConnection()
            asyncCall()
            print("Si paso")
        if arduino:
           
           st.session_state.success = True
           st.session_state.failure = False
           st.session_state.disabled = True
           st.session_state.expButton = False
        else:
              st.session_state.success = False
              st.session_state.failure = True
        st.session_state.clicked = False
        st.rerun()  
           #dataRetrieval(arduino)
    if st.session_state.success:
        st.success("✅ Conexión establecida")
    if st.session_state.failure:
        st.error("❌ No se detectó Arduino")
        

         
        
   
        
