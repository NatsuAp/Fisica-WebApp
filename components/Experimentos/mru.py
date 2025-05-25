import streamlit as st
from Utils import pageManager
import pandas as pd
from data import arduinoDataManager
from PIL import Image
import time
from data import questionBank

    
def goBack():
    for x in range(5, 0, -1):
            msg = f"Respuesta enviada\n Volviendo al menu en {x} segundos"
            st.success(msg)
            time.sleep(1)
            st.session_state.clear
    pageManager.page = "homepage"
    st.rerun()
def checkQuestionsMissing():
    for i in st.session_state.values():
        if i =="" or i =="NULL":
            st.session_state.continuar = True
            return True
    return False
def deployMRU():
    if "continuar" not in st.session_state:
        st.session_state.continuar = False
    if "seguro" not in st.session_state:
        st.session_state.seguro = False    
    if "ans_2_a" not in st.session_state:
        st.session_state.ans_2_a = None
    if "ans_2_b" not in st.session_state:
        st.session_state.ans_2_b = None
    if "ans_2_c" not in st.session_state:
        st.session_state.ans_2_c = None
    if "ans_2_d" not in st.session_state:
        st.session_state.ans_2_d = None
    if "pregunta_7" not in st.session_state:
        st.session_state.pregunta_7 =  questionBank.escoger_pregunta_aleatoria()
        
    st.title("Laboratorio de Movimiento Rectilineo Uniforme (MRU)")
    st.markdown(
        """
                ### Objetivo:
- Determinar gráficamente el valor de la velocidad media de un cuerpo en MRU.
- Conocer cómo está descrito el movimiento de los cuerpos en MRU.
- Aplicar los conceptos del movimiento de los cuerpos en MRU.

### Introducción:
En esta práctica analizaremos el movimiento rectilíneo uniforme o MRU, el cual nos permite estudiar todos los cuerpos que se mueven con **rapidez constante** o **velocidad constante** o cuya **fuerza neta aplicada sea cero**.  
Para este tipo de movimiento podemos definir la rapidez media como:
                """
    )

    st.latex(
        r"""
             v_{\text{media}} = \frac{x_{\text{final}} - x_{\text{inicial}}}{t_{\text{final}} - t_{\text{inicial}}}

             """
    )
    st.markdown(
        """
                ### Materiales:
- Cinta métrica.
- Tubo con agua.
- Cronómetro.
- Rampa inclinada.

### Procedimiento:
Para la realización adecuada de esta práctica de laboratorio relacionada a MRU debemos tener los materiales indicados anteriormente. Primero realizamos el montaje, el cual consiste en tomar la rampa graduada suministrada por el profesor y seleccionar un ángulo deseado.

1. Seleccione el ángulo de inclinación.
2. Inicie el experimento


                """
    )
    st.markdown(
        """
                ### Análisis de resultados y datos
                """
    )
    st.caption(
        "La informacion conseguida se mostrara aqui cuando se realize el expermimento"
    )

    st.markdown("**Tabla #1** Tiempo transcurrido en cada marca")
    tiempo = arduinoDataManager.runDataTiempo()
    posicion = arduinoDataManager.runDataPosicion()
    # tablaTiempo = st.data_editor(tiempo)
    st.table(tiempo)
    
    st.markdown("**Tabla #2** Tiempo transcurrido en cada marca")
    # tablaPosicion = st.data_editor(posicion)
    st.table(posicion)
    st.markdown(
        """
              ####  1. **(0.5 Puntos)** Con los datos de la Tabla #2 dibuje un gráfico de posición **x(cm)** (eje vertical) vs. tiempo **t(s)** (eje horizontal). Use la escala apropiada en el diseño de su gráfico.

                """
    )

    with st.container(border=True):
        st.markdown(
            """
                
                ### Imagen de Grafico dibujado
            
            """
        )
        st.file_uploader(
            "Procure que su imagen sea visible", accept_multiple_files=False, key="ans_1"
        )
        if st.session_state.ans_1 is not None:
            try:
                image = Image.open(st.session_state.ans_1)
                image.verify()
                st.success("✅ ¡Archivo cargado exitosamente!")
                st.image(st.session_state.ans_1)
                
            except Exception as e:

                st.error(
                    "❌ El archivo que has subido no es una imagen válida. Por favor, selecciona un archivo en formato JPG, PNG o similar."
                )

    # PREGUNTA 2

    st.markdown(
        """
                   #### 2. **(0.5 Puntos)** Calcule el valor de la pendiente para cuatro pares de puntos diferentes de la recta dibujada en el punto 1.

                    """
    )
    col1, col2 = st.columns(2, border=True)
    col3, col4 = st.columns(2, border=True)

    with col1:
        col1a, col2a = st.columns(2)
        col1a.latex(
            r"""P_1 = \frac{x_2 - x_1}{t_2 - t_1} =
"""
        )
        st.session_state.ans_2_a=col2a.text_input(label="Respuesta:", key="ans2_a")
        col1a_x2_x1, col1a_t2_t1 = st.columns(2)
        ans_2_x2_a=col1a_x2_x1.text_input(label="X2:", key="x2_ans2_a")
        ans_2_t2_a=col1a_x2_x1.text_input(label="T2:", key="t2_ans2_a")
        ans_2_x1_a=col1a_t2_t1.text_input(label="X1:", key="x1_ans2_a")
        ans_2_t1_a=col1a_t2_t1.text_input(label="T1:", key="t1_ans2_a")
    with col2:
        col1b, col2b = st.columns(2)
        col1b.latex(
            r"""P_2 = \frac{x_2 - x_1}{t_2 - t_1} =
"""
        )
        st.session_state.ans_2_b=col2b.text_input(label="Respuesta:", key="ans2_b")
        col1b_x2_x1, col1b_t2_t1 = st.columns(2)
        ans_2_x2_b=col1b_x2_x1.text_input(label="X2:", key="x2_ans2_b")
        ans_2_t2_b=col1b_x2_x1.text_input(label="T2:", key="t2_ans2_b")
        ans_2_x1_b=col1b_t2_t1.text_input(label="X1:", key="x1_ans2_b")
        ans_2_t1_b=col1b_t2_t1.text_input(label="T1:", key="t1_ans2_b")
    with col3:
        col1c, col2c = st.columns(2)
        col1c.latex(
            r"""P_3 = \frac{x_2 - x_1}{t_2 - t_1} =
"""
        )
        st.session_state.ans_2_c=col2c.text_input(label="Respuesta:", key="ans2_c")
        col1c_x2_x1, col1c_t2_t1 = st.columns(2)
        ans_2_x2_c=col1c_x2_x1.text_input(label="X2:", key="x2_ans2_c")
        ans_2_t2_c=col1c_x2_x1.text_input(label="T2:", key="t2_ans2_c")
        ans_2_x1_c=col1c_t2_t1.text_input(label="X1:", key="x1_ans2_c")
        ans_2_t1_c=col1c_t2_t1.text_input(label="T1:", key="t1_ans2_c")
    with col4:
        col1d, col2d = st.columns(2)
        col1d.latex(
            r"""P_4 = \frac{x_2 - x_1}{t_2 - t_1} =
"""
        )
        st.session_state.ans_2_d=col2d.text_input(label="Respuesta:", key="ans1_d")
        col1d_x2_x1, col1d_t2_t1 = st.columns(2)
        ans_2_x2_d=col1d_x2_x1.text_input(label="X2:", key="x2_ans2_d")
        ans_2_t2_d=col1d_x2_x1.text_input(label="T2:", key="t2_ans2_d")
        ans_2_x1_d=col1d_t2_t1.text_input(label="X1:", key="x1_ans2_d")
        ans_2_t1_d=col1d_t2_t1.text_input(label="T1:", key="t1_ans2_d")

    st.session_state.ans_2_a = "#x2=" + ans_2_x2_a + "#x1=" + ans_2_x1_a + "#t2=" + ans_2_t2_a + "#t1=" + ans_2_t1_a + "#ans=" + st.session_state.ans_2_a
    st.session_state.ans_2_b = "#x2=" + ans_2_x2_b + "#x1=" + ans_2_x1_b + "#t2=" + ans_2_t2_b + "#t1=" + ans_2_t1_b + "#ans=" + st.session_state.ans_2_b
    st.session_state.ans_2_c = "#x2=" + ans_2_x2_c + "#x1=" + ans_2_x1_c + "#t2=" + ans_2_t2_c + "#t1=" + ans_2_t1_c + "#ans=" + st.session_state.ans_2_c
    st.session_state.ans_2_d = "#x2=" + ans_2_x2_d + "#x1=" + ans_2_x1_d + "#t2=" + ans_2_t2_d + "#t1=" + ans_2_t1_d + "#ans=" + st.session_state.ans_2_d
    
    # PREGUNTA 3

    st.markdown(
        """
              ####  3. **(0.5 Puntos)** ¿Qué significado físico (Magnitud física) tienen las pendientes de la recta calculada en el punto 2?

                """
    )

    st.text_area(label="Ingrese su respuesta", key="ans_3")
    
    # PREGUNTA 4

    st.markdown(
        """
               #### 4. **(0.5 Puntos)** ¿Los valores obtenidos de las pendientes son iguales o diferentes? Si respondes que son iguales, ¿por qué crees que sucede esto? O si respondes que son diferentes, ¿por qué sucede esto?

                """
    )

    st.text_area(label="Ingrese su respuesta", key="ans_4")

    # PREGUNTA 5

    st.markdown(
        """
                #### 5. **(0.5 Puntos)** Con cada valor de la pendiente obtenida en el ítem 2, y los primeros 4 tiempos usados en la Tabla #2 construya la siguiente Tabla #3.
                """
    )

    tablaDatos = arduinoDataManager.runData5()
    tabla5 = st.data_editor(tablaDatos, disabled=[""])
    
    # a = tabla5.loc[tabla5["t1"]]
    #favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    # https://docs.streamlit.io/develop/api-reference/data/st.data_editor

    st.markdown(
        """
                A partir de los datos de la Tabla #3 realice un gráfico de velocidad **v(cm/s)** (eje vertical) vs tiempo **t(s)** (eje horizontal).

                """
    )

    with st.container(border=True):
        st.markdown(
            """
                
                ### Imagen de Grafico dibujado
            
            """
        )

        st.file_uploader(
            "Procure que su imagen sea visible", accept_multiple_files=False, key="ans_5_b"
        )

        if st.session_state.ans_5_b is not None:
            try:

                image_2 = Image.open(st.session_state.ans_5_b)
                image_2.verify()
                st.success("✅ ¡Archivo cargado exitosamente!")
                st.image(st.session_state.ans_5_b)
                
                # st.rerun()
            except Exception as e:

                st.error(
                    "❌ El archivo que has subido no es una imagen válida. Por favor, selecciona un archivo en formato JPG, PNG o similar."
                )

            # PREGUNTA 6

    st.markdown(
        """
             ####   6. **(0.5 Puntos)** ¿Qué puede comentar acerca del gráfico de velocidad vs tiempo? ¿Es una línea horizontal?, ¿es una línea que no es completamente horizontal? Explique sus respuestas.

                """
    )
    st.text_area(label="Ingrese su respuesta", key="ans_6")
     
    # PREGUNTA 7

    # st.write(st.session_state.pregunta_7)

    st.markdown(
        """## Ejercicio de aplicación de lo aprendido en esta práctica de laboratorio \n """
        + st.session_state.pregunta_7["enunciado"]
    )

    st.radio(
        "### 7." + st.session_state.pregunta_7["pregunta"],
        st.session_state.pregunta_7["opciones"],
        index=None, key="ans_7"
    )
    st.session_state.pregunta_7["respuesta_correcta"]
    
    # PREGUNTA 8

    st.markdown(
        """
            ####    8. **(1.0 Punto)** Con la elección de las dos ecuaciones en la pregunta anterior, resuelva el sistema de ecuaciones y encuentre el tiempo \( t \) y posición final \( x_f \) en la que los dos se encuentran. Realice de forma ordenada sus cálculos.

                """
    )

    st.file_uploader(
            "Procure que su imagen sea visible y tenga buena calidad", accept_multiple_files=False, key="ans_8"
        )

    if st.session_state.ans_8 is not None:
            try:

                image_3 = Image.open(st.session_state.ans_8)
                image_3.verify()
                st.success("✅ ¡Archivo cargado exitosamente!")
                st.image(st.session_state.ans_8)
                # st.rerun()
            except Exception as e:

                st.error(
                    "❌ El archivo que has subido no es una imagen válida. Por favor, selecciona un archivo en formato JPG, PNG o similar."
                )
                
    st.markdown("""  
                #### 9. **(0.5 Puntos)** Conclusiones: Realice una breve conclusión de su Laboratorio de MRU
                """)
    st.text_area("Ingrese su respuesta", key="ans_9")
    
    
    #st.write(st.session_state)
    if st.session_state.continuar:
        st.warning("⚠️ Dejaste algunas preguntas sin resolver, estas seguro que quieres continuar?")
    if st.button("Enviar Respuesta", key="final"):
        
        st.session_state.continuar = checkQuestionsMissing()
        
        if not st.session_state.continuar:
            goBack()
        if st.session_state.seguro:
            st.session_state.continuar= False
            goBack()
        st.session_state.seguro = True
        st.rerun()
        
            
            
        
            

