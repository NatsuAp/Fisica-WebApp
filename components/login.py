import shutil
import streamlit as st
import time
import Utils.pageManager as pageManager
import os
# from arduino.connection import checkConnection, asyncCall
def checkInput():
    try:
        if st.session_state.numEstu>8:
            st.error("Numero de estudiantes Excedido")
            st.session_state.x = False
       
        if st.session_state.numEstu <1:
            st.session_state.x = False
    except Exception as e:
        st.session_state.x=False
    st.session_state.x = True
def deployLoginPage():
    try:
        shutil.rmtree("temp_images")
    except Exception as e:
        print(e)

    if "numEstu" not in st.session_state:
         st.session_state.numEstu = None
    if "x" not in st.session_state:
         st.session_state.x = True
    if "clicked" not in st.session_state:
        st.session_state.clicked = False
    datos = []
    nombreEstudiantes = []
    st.title("***Para empezar ingresa tus datos***")
    with st.container(border=True):
        st.header("Ingrese los siguientes datos:")
        st.write("Numero de Integrantes:")
        st.session_state.numEstu = st.number_input("Numero de Integrantes", value=1, step=1,format="%01d", on_change=checkInput, min_value=1)

        if st.session_state.x:
            for i in range(1,st.session_state.numEstu+1):
                nombreEstu= st.text_input(f"Nombre del Estudiante {i}")
                nombreEstudiantes.append(nombreEstu)
            correoEstu = st.text_input("Ingerese el Correo de un Estudiante:")
            
        st.write("Datos del profesor:")
        nombreProf = st.text_input("Nombre del Profesor")
        correoProf = st.text_input("Correo del Profesor")
        

        if st.button("Confirmar"):
            st.session_state.clicked = True

        if st.session_state.clicked:
            datos.append(nombreEstudiantes)
            datos.append(correoEstu)
            
            datos.append(nombreProf)   
            datos.append(correoProf)
           

            f = open("Utils/loginData.txt", "w+")
            
            nombres =""
            for i in nombreEstudiantes:
                nombres+= i + " , "

            f.write(nombres+ "\n")
            f.write(correoEstu+ "\n")
            f.write(nombreProf+ "\n")
            f.write(correoProf+ "\n")
            if any(map(lambda x: x=="", datos)):
                st.warning("⚠️ ¡Faltan campos por completar! 📝 Por favor, llena todos los datos requeridos antes de continuar. ✍️")
            else:
                st.success("✔️ Datos completos. Guardado exitoso. 💽")
                with st.spinner("Cargando", show_time=False):
                        time.sleep(1.6)
                        pageManager.page = "mainpage"
                        st.rerun()
          
               
    
   
                    
              
       
   
    
 
