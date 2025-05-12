import streamlit as st
from arduino.connection import checkConnection, dataRetrieval
import Utils.pageManager as pageManager
def deployMainPage():
    
    
    st.title("***Conecta el arduino***")
    
    if st.button('Iniciar Conexion'):
       
       arduino = checkConnection()
       if arduino:
           #dataRetrieval(arduino)
           st.write("Conexion realizada correctamente")
           if st.button("Iniciar experimento"):
               pageManager.page="homepage"
               st.rerun()
        
       else:
              container = st.container()
              container.write("No se ha detectado arduino")
        
         
        
   
        
