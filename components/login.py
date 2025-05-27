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
        st.session_state.x=True
    
def deployLoginPage():
   
    if "numEstu" not in st.session_state:
         st.session_state.numEstu = None
    if "x" not in st.session_state:
         st.session_state.x = False
    if "clicked" not in st.session_state:
        st.session_state.clicked = False
    if "nombreEstudiantes" not in st.session_state:
        st.session_state.nombreEstudiantes = []
    datos = []
    nombreEstudiantes = []
    nombre_Profesor = ""
    st.title("***Para empezar ingresa tus datos***")
    with st.container(border=True):
        st.header("Ingrese los siguientes datos:")
        st.write("Numero de Integrantes:")
        st.session_state.numEstu = st.number_input("Numero de Integrantes", value=1, step=1,format="%01d", on_change=checkInput, min_value=1)

        if st.session_state.x:
            for i in range(1,st.session_state.numEstu+1):
                nombreEstu= st.text_input(f"Nombre del Estudiante {i}")
                nombreEstudiantes.append(nombreEstu)
            correoEstu = st.text_input("Ingrese el Correo de un Estudiante:")
           
        st.write("Datos del profesor:")
        nombre_Profesor=st.text_input("Nombre del Profesor", key="nombre_Profesor")
        nombreEstudiantes.append(nombre_Profesor)
        print(st.session_state.nombre_Profesor)
        correoProf = st.text_input("Correo del Profesor", key="correo_Profesor")
        
        if st.button("Confirmar"):
            st.session_state.clicked = True
            
        if st.session_state.clicked:
            datos.append(nombreEstudiantes)
            datos.append(correoEstu)
            datos.append(st.session_state.nombre_Profesor)   
            datos.append(correoProf)
            
            st.session_state.nombre_Profesor 
            if any(map(lambda x: x=="", datos)):
                st.warning("⚠️ ¡Faltan campos por completar! 📝 Por favor, llena todos los datos requeridos antes de continuar. ✍️")
            else:
                st.session_state.nombreEstudiantes =nombreEstudiantes
                
                print(st.session_state.nombre_Profesor)
                st.success("✔️ Datos completos. Guardado exitoso. 💽")
                with st.spinner("Cargando", show_time=False):
                        time.sleep(1.6)
                        pageManager.page = "mainpage"
                        st.rerun()
          
               
    
   
                    
              
       
   
    
 
