import streamlit as st
# from arduino.connection import checkConnection
from Utils import pageManager
def deployWarningPage():
    st.error('Se ha perdido la conexion inesperadamente con el arduino  \n\n Reconecta el arduino para continuar' , icon="⚠️")
    #TODO: para reconectar si se pierde la conexion con el arduino
    if st.button("Reconectar"):
        with st.spinner("Estableciendo conexión", show_time=True):
            arduino = checkConnection()
            arduino = True
        if arduino:
            pageManager.page = "homepage"
            st.rerun()
        
            