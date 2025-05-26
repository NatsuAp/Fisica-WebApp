import streamlit as st
import time
import Utils.pageManager as pageManager
# from arduino.connection import checkConnection, asyncCall
def checkInput():
    try:
        if st.session_state.numEstu>8:
            st.error("Numero de estudiantes Excedido")
            st.session_state.x = False
        else:
            st.session_state.x = True
        if st.session_state.numEstu <1:
            st.session_state.x = False
    except Exception as e:
        st.session_state.x=False
    
def deployLoginPage():
    if "numEstu" not in st.session_state:
         st.session_state.numEstu = None
    if "x" not in st.session_state:
         st.session_state.x = False
    if "clicked" not in st.session_state:
        st.session_state.clicked = False
    datos = []
    nombreEstudiantes = []
    st.title("***Para empezar ingresa tus datos***")
    with st.container(border=True):
        st.header("Ingrese los siguientes datos:")
        st.write("Numero de Integrantes:")
        st.session_state.numEstu = st.number_input("Numero de Integrantes", value=None, step=1,format="%01d", on_change=checkInput, min_value=0)

        if st.session_state.x:
            for i in range(1,st.session_state.numEstu+1):
                nombreEstu= st.text_input(f"Nombre del Estudiante {i}")
                nombreEstudiantes.append(nombreEstu)
            correoEstu = st.text_input("Ingerese el Correo de un Estudiante:")
            confirmEstu = st.text_input("Confirma tu Correo")
        st.write("Datos del profesor:")
        nombreProf = st.text_input("Nombre del Profesor")
        correoProf = st.text_input("Correo del Profesor")
        
        confirmProf = st.text_input("Confirma el Correo")

        if st.button("Confirmar"):
            st.session_state.clicked = True

        if st.session_state.clicked:
            datos.append(nombreEstudiantes)
            datos.append(correoEstu)
            datos.append(confirmEstu)
            datos.append(nombreProf)   
            datos.append(correoProf)
            datos.append(confirmProf)

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
          
               
    
   
                    
              
       
   
    
 
