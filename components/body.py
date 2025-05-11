import streamlit as st
from data import data
import Utils.pageManager as pageManager


def deployBody():
    st.header("Grafica Velocidad vs Tiempo")
    data.runData()
    st.write("#Pregunta")
    st.write("A.  Respuesta A")
    st.write("B.  Respuesta B")
    st.write("C.  Respuesta C")
    st.write("D.  Respuesta D")
    if st.button("Volver"):
        pageManager.page = "mainPage"
        st.rerun()



    
