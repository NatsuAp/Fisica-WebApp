import threading
import time
import streamlit as st
from arduino.connection import checkConnection, asyncCall
import Utils.pageManager as pageManager

   
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
        
        
    st.title("***Conecta el arduino***")
    if st.session_state.counter>2 and not st.session_state.success:
            st.session_state.failure = False
            st.warning(st.session_state.warningMessage)
            st.session_state.userPort = st.text_input("Ingrese puerto. (COM3, COM4)")
    
    if st.button('Iniciar conexión', key="conexion", disabled=st.session_state.disabled):
            st.session_state.clicked = True
            st.rerun()
    
    
    
        
    if st.button("Iniciar experimento", disabled=st.session_state.expButton):
               pageManager.page="homepage"
               st.rerun()
    
    
    if st.session_state.clicked:
        with st.spinner("Estableciendo conexión", show_time=True):
            if not st.session_state.userPort:
                print("hola")
                arduino = checkConnection()
            else:
                arduino = checkConnection(st.session_state.userPort)
            
            
            print("Si paso")
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
              if st.session_state.counter > 3: st.session_state.warningMessage = "⚠️Error de conexión: el puerto ingresado no es válido o no se encuentra disponible. \n\n  ⚙️Ejemplo de formato válido: COM3 (Windows) o /dev/ttyUSB0 (Linux)."

        st.session_state.clicked = False
        st.rerun()  
           #dataRetrieval(arduino)
    if st.session_state.success:
        st.success("✅ Conexión establecida")
    if st.session_state.failure:
        st.error("❌ No se detectó Arduino")
        

         
        
   
        
