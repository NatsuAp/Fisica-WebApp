from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Image
import streamlit as st
from data import sendData
def crear_laboratorio_mru_pdf(
    nombre_archivo,
    nombreProfesor,
    nombreEstudiante,
    fecha,
    datosArduino,
    correo
    ):
   


   

    doc = SimpleDocTemplate("pdfs/Experimento_MRU.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    contenido = []

    # Encabezado
    contenido.append(
        Paragraph(
            "**Laboratorio de Movimiento Uniformemente Rectilíneo (MUR)**",
            styles["Title"],
        )
    )
    
    nombre = ""
    
    contenido.append(
        Paragraph("Profesores:" + nombreProfesor + " - Física I", styles["Normal"])
    )
    contenido.append(Paragraph("Colegio San José de Barranquilla", styles["Normal"]))
    contenido.append(Spacer(1, 12))
    contenido.append(Paragraph("Integrantes: " + nombreEstudiante, styles["Normal"]))
    contenido.append(
        Paragraph(
            "________________________________________________________ Fecha: " + str(fecha),
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 12))

    # Objetivo
    contenido.append(Paragraph("**Objetivo:**", styles["Heading2"]))
    objetivos = [
        "Determinar gráficamente el valor de la velocidad media de un cuerpo en MRU.",
        "Conocer cómo está descrito el movimiento de los cuerpos en MRU.",
        "Aplicar los conceptos del movimiento de los cuerpos en MRU.",
    ]
    for obj in objetivos:
        contenido.append(Paragraph("● " + obj, styles["Normal"]))

    # Introducción
    contenido.append(Spacer(1, 12))
    contenido.append(Paragraph("**Introducción:**", styles["Heading2"]))
    contenido.append(
        Paragraph(
            "En esta práctica analizaremos el movimiento rectilíneo uniforme o MRU, el cual nos permite estudiar "
            "todos los cuerpos que se mueven con rapidez constante o cuya fuerza neta aplicada sea cero.",
            styles["Normal"],
        )
    )
    contenido.append(
        Paragraph(
            "La rapidez media se define como: v = (x<sub>f</sub> - x<sub>i</sub>) / (t<sub>f</sub> - t<sub>i</sub>)",
            styles["Normal"],
        )
    )

    # Materiales
    contenido.append(Spacer(1, 12))
    contenido.append(Paragraph("**Materiales:**", styles["Heading2"]))
    materiales = ["Cinta métrica", "Tubo con agua", "Cronómetro", "Rampa inclinada"]
    for mat in materiales:
        contenido.append(Paragraph("● " + mat, styles["Normal"]))

    # Procedimiento
    contenido.append(Spacer(1, 12))
    contenido.append(Paragraph("**Procedimiento:**", styles["Heading2"]))
    pasos = [
        "Seleccione el ángulo de inclinación.",
        "Observe cómo la burbuja de aire se mueve y mida el tiempo cuando este pase por cada marca de 10 cm.",
        "Registre todos sus datos en la Tabla #1.",
        "Tome dos veces los datos.",
    ]
    for paso in pasos:
        contenido.append(Paragraph(paso, styles["Normal"]))

    # Tabla 1 (esqueleto)
    contenido.append(Spacer(1, 12))
    contenido.append(
        Paragraph("**Tabla #1: Tiempo transcurrido en cada marca**", styles["Heading3"])
    )
    tabla1 = Table(
        [
            [
                "Tiempo (s)",
                "t1 (10 cm)",
                "t2 (20 cm)",
                "t3 (30 cm)",
                "t4 (40 cm)",
                "t5 (50 cm)",
                "t6 (60 cm)",
                "t7 (70 cm)",
            ],
            ["T1", "", "", "", "", "", "", ""],
            ["T2", "", "", "", "", "", "", ""],
            ["T = (T1+T2)/2", "", "", "", "", "", "", ""],
        ]
    )
    tabla1.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 1, colors.black)]))
    contenido.append(tabla1)

    # Preguntas de análisis
    contenido.append(Spacer(1, 12))
    contenido.append(
        Paragraph("**Análisis de resultados y datos**", styles["Heading2"])
    )
   
    #PREGUNTA 1
    contenido.append(Paragraph("1. (0.5 Puntos) Dibuje un gráfico de posición vs tiempo con los datos de la Tabla #2.", styles["Normal"]))
    try:
        img = Image(st.session_state.img_ans_1)
        img._restrictSize(400, 300)
    except Exception as e:
        img = None
    
    contenido.append(img)
    contenido.append(Spacer(1, 8))
    #PREGUNTA 2
    contenido.append(Paragraph("2. (0.5 Puntos) Calcule la pendiente de 4 pares de puntos diferentes de la recta.", styles["Normal"]))
    respuesta_usuario_2 = st.session_state.ans_2_a + " " + st.session_state.ans_2_b + " " + st.session_state.ans_2_c + " " + st.session_state.ans_2_d
    respuesta_usuario_2 = respuesta_usuario_2.replace("#", " ")
    contenido.append(Paragraph(f"<b>Respuesta:</b> {respuesta_usuario_2}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    #PREGUNTA 3
    contenido.append(Paragraph("3. (0.5 Puntos) ¿Qué significado físico tienen las pendientes calculadas?", styles["Normal"]))
    
    contenido.append(Paragraph(f"<b>Respuesta:</b> {st.session_state.ans_3}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    #PREGUNTA 4
    
    contenido.append(Paragraph("""4. (0.5 Puntos) ¿Los valores obtenidos de las pendientes son iguales o diferentes? Si respondes que son
iguales, ¿por qué crees que sucede esto? ó si respondes que son diferentes ¿por qué sucede esto?""", styles["Normal"]))
    
    contenido.append(Paragraph(f"<b>Respuesta:</b> {st.session_state.ans_4}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    #PREGUNTA 5
    
    contenido.append(Paragraph("5. (0.5 Puntos) Con cada pendiente, complete la Tabla #3 de velocidades medias.", styles["Normal"]))
    
    #contenido.append(Paragraph(f"<b>Respuesta:</b> {st.session_state.ans_4}", styles["Normal"]))  TODO: TABLA
    # Tabla 3
    # contenido.append(Spacer(1, 12))
    # contenido.append(Paragraph("**Tabla #3: Velocidades medias**", styles["Heading3"]))
    # tabla3 = Table(
    #     [
    #         ["Tiempos t(s)", "t1", "t2", "t3", "t4"],                                             #Este es un ejemplo de como hacerla
    #         ["Velocidades v(cm/s)", "", "", "", ""],
    #     ]
    # )
    # tabla3.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 1, colors.black)]))
    # contenido.append(tabla3)
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph("A partir de los datos de la tabla realice un grafico de velocidad vs tiempo", styles["Normal"]))

    try:
        img_2 = Image(st.session_state.img_ans_2)
        img_2._restrictSize(400, 300)
    except Exception as e:
        img_2 = None
    
    contenido.append(img_2)
    contenido.append(Spacer(1, 8))
    #PREGUNTA 6
    contenido.append(Paragraph("6. (0.5 Puntos) ¿Qué puede comentar acerca del gráfico de velocidad vs tiempo? ¿Es una línea horizontal?, ¿es una línea que no es completamente horizontal? Explique sus respuestas.", styles["Normal"]))
    
    contenido.append(Paragraph(f"<b>Respuesta:</b> {st.session_state.ans_6}", styles["Normal"]))
    
    # Ejercicio de aplicación
    contenido.append(PageBreak())
    contenido.append(Paragraph("**Ejercicio de aplicación:**", styles["Heading2"]))
    contenido.append(
        Paragraph(
            st.session_state.pregunta_7["enunciado"],
            styles["Normal"],
        )
    )
    contenido.append(
        Paragraph(
            "### 7." + st.session_state.pregunta_7["pregunta"],
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 8))
    
    for opcion in st.session_state.pregunta_7["opciones"]:
        contenido.append(Paragraph(opcion, styles["Normal"]))
        contenido.append(Spacer(1, 4))  
    
    respuesta_usuario_7 = st.session_state.get("ans_7", None)
    
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {respuesta_usuario_7}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    
    

    contenido.append(
        Paragraph(
            "8. (1.0 Punto) Con la elección de las dos ecuaciones en la pregunta anterior, resuelva el sistema de ecuaciones y encuentre el tiempo ( t ) y posición final ( x_f ) en la que los dos se encuentran. Realice de forma ordenada sus cálculos.",
            styles["Normal"],
        )
    )
    try:
        img_3 = Image(st.session_state.img_ans_3)
        img_3._restrictSize(400, 300)
    except Exception as e:
        img_3 = None
    
    contenido.append(img_3)
    contenido.append(Spacer(1, 8))
    contenido.append(
        Paragraph(
            "9. (0.5 Puntos) Conclusiones: Realice una breve conclusión de su Laboratorio de MRU", styles["Normal"]
        )
    )
    contenido.append(Spacer(1, 8))
    
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {st.session_state.ans_9}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    
    contenido.append(
        Paragraph(
            "### 10." + st.session_state.pregunta_10["question"],
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 8))
    
    for clave, texto in st.session_state.pregunta_10["options"].items():
        contenido.append(Paragraph(f"{clave}. {texto}", styles["Normal"]))
        contenido.append(Spacer(1, 4))
    
   
    
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {st.session_state.ans_10}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    
    contenido.append(
        Paragraph(
            "### 11." + st.session_state.pregunta_11["question"],
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 8))
    
    for clave, texto in st.session_state.pregunta_11["options"].items():
        contenido.append(Paragraph(f"{clave}. {texto}", styles["Normal"]))
        contenido.append(Spacer(1, 4))
    
   
    
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {st.session_state.ans_11}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    
    contenido.append(
        Paragraph(
            "### 12." + st.session_state.pregunta_12["question"],
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 8))
    
    for clave, texto in st.session_state.pregunta_12["options"].items():
        contenido.append(Paragraph(f"{clave}. {texto}", styles["Normal"]))
        contenido.append(Spacer(1, 4))  
    
   
    
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {st.session_state.ans_12}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    
    contenido.append(
        Paragraph(
            "### 13." + st.session_state.pregunta_13["question"],
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 8))
    
    for clave, texto in st.session_state.pregunta_13["options"].items():
        contenido.append(Paragraph(f"{clave}. {texto}", styles["Normal"]))
        contenido.append(Spacer(1, 4))
    
   
    
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {st.session_state.ans_13}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    
    contenido.append(
        Paragraph(
            "### 14." + st.session_state.pregunta_14["question"],
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 8))
    
    for clave, texto in st.session_state.pregunta_14["options"].items():
        contenido.append(Paragraph(f"{clave}. {texto}", styles["Normal"]))
        contenido.append(Spacer(1, 4))
    
   
    
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {st.session_state.ans_14}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    
    contenido.append(
        Paragraph(
            "### 15." + st.session_state.pregunta_15["question"],
            styles["Normal"],
        )
    )
    contenido.append(Spacer(1, 8))
    
    for clave, texto in st.session_state.pregunta_15["options"].items():
        contenido.append(Paragraph(f"{clave}. {texto}", styles["Normal"]))
        contenido.append(Spacer(1, 4))  
    
   
    
    contenido.append(Spacer(1, 8))
    contenido.append(Paragraph(f"<b>Respuesta seleccionada:</b> {st.session_state.ans_15}", styles["Normal"]))
    contenido.append(Spacer(1, 8))
    

    doc.build(contenido)
    st.success(f"📄 Documento creado exitosamente!")
    
    try:
        sendData.enviar_pdf_por_correo(correo, nombreEstudiante)
        return True
    except Exception as e:
        return False
        
