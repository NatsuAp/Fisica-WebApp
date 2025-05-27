import streamlit as st

from Utils import pageManager
from arduino.connection import asyncCall, checkConnection
def deployWarningPage():
    st.error('Se ha perdido la conexion inesperadamente con el arduino  \n\n Reconecta el arduino para continuar' , icon="⚠️")
   
    if st.button("Reconectar"):
        with st.spinner("Estableciendo conexión", show_time=True):
            arduino = checkConnection(None)
            if arduino is None or "userError":
                st.warning("No se encontro el arduino")
            #arduino = True
        if arduino:
            asyncCall()
            pageManager.page = "homepage"
            st.rerun()
        
            