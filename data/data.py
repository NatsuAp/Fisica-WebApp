import pandas as pd
import streamlit as st
import numpy as np
#Funcion para simular informacion
def runData():
    chart_data = pd.DataFrame(np.random.randn(20, 1), columns=["Velocidad"])
    st.line_chart(chart_data)