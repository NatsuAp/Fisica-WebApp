import streamlit as st
import time
import Utils.pageManager as pageManager
from arduino.connection import checkConnection, asyncCall
def deployLoginPage():

    datos = []
    st.title("***Para empezar ingresa tus datos***")
    with st.form("Datos", enter_to_submit=False):
        st.header("Ingrese los siguientes datos:")
        st.write("Datos del estudiante:")
        nombreEstu= st.text_input("Nombre del Estudiante")
        correoEstu = st.text_input("Correo del Estudiante")
        confirmEstu = st.text_input("Confirma tu Correo")
        st.write("Datos del profesor:")
        nombreProf = st.text_input("Nombre del Profesor")
        correoProf = st.text_input("Correo del Profesor")
        confirmProf = st.text_input("Confirma el Correo")
        submitted = st.form_submit_button("Confirmar")
        datos.append(nombreEstu)
        datos.append(correoEstu)
        datos.append(confirmEstu)
        datos.append(nombreProf)    
        datos.append(correoProf)
        datos.append(confirmProf)
        if submitted:
            if any(map(lambda x: x=="", datos)):
                st.warning("⚠️ ¡Faltan campos por completar! 📝 Por favor, llena todos los datos requeridos antes de continuar. ✍️")
                 
            elif (correoEstu!=confirmEstu) or (correoProf!=confirmProf):
                st.warning("⚠️ Los correos electrónicos no coinciden. 📧 Por favor, verifica ambos campos. 🔍")
            else:
                st.success("✔️ Datos completos. Guardado exitoso. 💽")
                with st.spinner("Cargando", show_time=False):
                        time.sleep(1.6)
                        pageManager.page = "mainpage"
                        st.rerun()
          
               
    
   
                    
              
       
   
    
 
