import pandas as pd
import streamlit as st
import numpy as np
#Funcion para simular informacion
columnasTiempo = [
        "Tiempo (s)",
        "t₁ (10 cm)",
        "t₂ (20 cm)",
        "t₃ (30 cm)",
        "t₄ (40 cm)",
        "t₅ (50 cm)",
        "t₆ (60 cm)",
        "t₇ (70 cm)",
    ]

columnasPosicion = [
        "Posiciones x(cm)",
        "10 cm",
        "20 cm",
        "30 cm",
        "40 cm",
        "50 cm",
        "60 cm",
        "70 cm",
    ]

datosTiempo = [
        ["T1", "", "", "", "", "", "", ""],
        ["T2", "", "", "", "", "", "", ""],
        ["T = (T1+T2)/2", "", "", "", "", "", "", ""],
    ]
datosPosicion = [["Tiempos t(s)", "", "", "", "", "", "", ""]]

columnasTiempo5 = ["", "t1 =", "t2 =", "t3 =", "t4 ="]
datos5 = [
    ["Velocidades v(cm/s)", "", "", "", ""],
    ["Tiempos t(s)", "", "", "", ""]
]
def runDataTiempo():
    tablaTiempo = pd.DataFrame(datosTiempo, columns=columnasTiempo)
    return tablaTiempo
def runDataPosicion():
    tablaPosicion = pd.DataFrame(datosPosicion, columns=columnasPosicion)
    return tablaPosicion
def runData5():
    tabla_3 = pd.DataFrame(datos5, columns=columnasTiempo5)
    return tabla_3