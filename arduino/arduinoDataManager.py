import pandas as pd
import streamlit as st
import numpy as np

from arduino.connection import checkConnection
#Funcion para simular informacion


columnasTiempo5 = ["", "t1 =", "t2 =", "t3 =", "t4 ="]
datos5 = [
    ["Velocidades v(cm/s)", "", "", "", ""],
    ["Tiempos t(s)", "", "", "", ""]
]
def runDataTiempo(datosTiempo, columnasTiempo):
    
    tablaTiempo = pd.DataFrame(datosTiempo, columns=columnasTiempo)
    return tablaTiempo
def runDataPosicion(datosPosicion, columnasPosicion):
    tablaPosicion = pd.DataFrame(datosPosicion, columns=columnasPosicion)
    return tablaPosicion
def runData5():
    tabla_3 = pd.DataFrame(datos5, columns=columnasTiempo5)
    return tabla_3



def dataRetrieval(tabla):
    arduino = checkConnection(None)
    print("checkconnection" + str(arduino))
    try:
        
        data = arduino.readline().decode('utf-8', errors='ignore').strip()
        print("Received line:", data)
        
        print(data)
        arr = data.split(" ")
        print(arr)
        f = open("Utils\expData.txt", "w+")
        f.write(str(arr[0])+ "\n")
        f.write(str(arr[1])+ "\n")
        
        if tabla=="tiempo":
            datosTiempo = [
        ["T1", 0, str(arr[1])],
        ["T = (T1+T2)/2", ""]
        ]
            columnasTiempo = [
        "Tiempo (s)",
        "t₁ (0 cm)",
        "t₂ ("+str(arr[0])+ " cm)",
        ]
            return runDataTiempo(datosTiempo, columnasTiempo) 
        else:
            columnasPosicion = [
        "Posiciones x(cm)",
        "0 cm",
        str(arr[0]) + " cm",
       
            ]
            datosPosicion = [["Tiempos t(s)", "0",str(arr[1]) ]]
            return runDataPosicion(datosPosicion, columnasPosicion)
    
        
    except Exception as e:
        print("error")
        print(e)
        return "inicia el experimento"
    
    
   
    #dataArr.insert(data)