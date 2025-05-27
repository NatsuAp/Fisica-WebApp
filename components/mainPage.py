import threading
import time
import streamlit as st
from arduino.connection import checkConnection, asyncCall
import Utils.pageManager as pageManager
def connectionButton(nombre, manual):
     if st.button(nombre, disabled=st.session_state.disabled):
            st.session_state.clicked = True
            if manual:
                 st.session_state.manualClick = True
     
   
def deployMainPage():
    
    if "counter" not in st.session_state:
        st.session_state.counter = 0
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
    if "warningMessage" not in st.session_state:
        st.session_state.warningMessage = "⚠️Conexión fallida tras múltiples intentos automáticos. \n\n 🔍Ingrese manualmente el puerto serial del Arduino para continuar."
    if "userPort" not in st.session_state:
        st.session_state.userPort = ""
    if "manualClick" not in st.session_state:
         st.session_state.manualClick = False    
        
    st.title("***Conecta el arduino***")
    if st.session_state.counter>2 and not st.session_state.success:
            st.session_state.failure = False
            st.warning(st.session_state.warningMessage)
            st.session_state.userPort = st.text_input("Ingrese puerto. (COM3, COM4)")
            col1, col2= st.columns(2)
            with col1:
                connectionButton("Conexion Manual", True)
                
            with col2:
                connectionButton("Conexion Automatica", False)  
                     
                  
    if st.session_state.counter<3:   
     connectionButton("Iniciar Conexion", False) 
     
    
    
    
        
    if st.button("Iniciar experimento", disabled=st.session_state.expButton):
               pageManager.page="homepage"
               st.rerun()
    
    
    if st.session_state.clicked:
        with st.spinner("Estableciendo conexión", show_time=True):
            if  st.session_state.manualClick:
                arduino = checkConnection(st.session_state.userPort)
                
            else:
                arduino = checkConnection(None)
                
           
            #arduino = True
        if arduino != "userError" and arduino is not None: 
           asyncCall()
           st.session_state.success = True
           st.session_state.failure = False
           st.session_state.disabled = True
           st.session_state.expButton = False
        else:
              st.session_state.counter = st.session_state.counter+1
              st.session_state.success = False
              st.session_state.failure = True
              if st.session_state.counter > 3:
                  if arduino == "userError": 
                    st.session_state.warningMessage = "⚠️Error de conexión: el puerto ingresado no es válido o no se encuentra disponible. \n\n  ⚙️Ejemplo de formato válido: COM3 (Windows) o /dev/ttyUSB0 (Linux)." 
                  else:
                    st.session_state.warningMessage = "⚠️Error de conexión: No se detecto ningun arduino \n\n  ⚙️Ejemplo de formato válido: COM3 (Windows) o /dev/ttyUSB0 (Linux)." 

        st.session_state.clicked = False
        st.session_state.manualClick = False
        st.rerun()  
           #dataRetrieval(arduino)
    
         

    if st.session_state.success:
        st.success("✅ Conexión establecida")
    if st.session_state.failure:
        st.error("❌ No se detectó Arduino")
        

         
        
   
        
