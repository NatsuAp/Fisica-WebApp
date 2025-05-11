import streamlit as st
from arduino.connection import checkConnection, dataRetrieval
import Utils.pageManager as pageManager
def deployMainPage():
    st.title("***Para iniciar el experimento conecta el arduino***")

    if st.button('Iniciar Conexion'):
       if checkConnection():
           dataRetrieval()
        
       else:
              container = st.container()
              container.write("No se ha detectado arduino")
        
         
        
    if st.button("Simular conexion"):
       pageManager.page="body"
       st.rerun()
        
