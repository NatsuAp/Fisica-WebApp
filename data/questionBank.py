import random
import json
import random
from pathlib import Path

def escoger_pregunta_aleatoria_7():
    with open("resources/preguntas.txt", "r", encoding="utf-8") as f:
        contenido = f.read()

    bloques = [bloque.strip() for bloque in contenido.split("### PREGUNTA_") if bloque.strip()]
    preguntas = []

    for bloque in bloques:
        lineas = bloque.splitlines()
        pregunta_dict = {}

        numero = lineas[0].strip(" #")
        pregunta_dict["id"] = int(numero)

        enunciado = ""
        pregunta = ""
        opciones = []
        respuesta = ""

        estado = None
        for linea in lineas[1:]:
            if linea.startswith("ENUNCIADO:"):
                estado = "enunciado"
                enunciado = linea.replace("ENUNCIADO:", "").strip()
            elif linea.startswith("PREGUNTA:"):
                estado = "pregunta"
                pregunta = linea.replace("PREGUNTA:", "").strip()
            elif linea.startswith("OPCIONES:"):
                estado = "opciones"
            elif linea.startswith("RESPUESTA_CORRECTA:"):
                estado = "respuesta"
                respuesta = linea.replace("RESPUESTA_CORRECTA:", "").strip()
            else:
                linea_limpia = linea.strip()
                if estado == "enunciado":
                    enunciado += " " + linea_limpia
                elif estado == "pregunta":
                    pregunta += " " + linea_limpia
                elif estado == "opciones" and linea_limpia:
                    opciones.append(linea_limpia)

        pregunta_dict["enunciado"] = enunciado
        pregunta_dict["pregunta"] = pregunta
        pregunta_dict["opciones"] = opciones
        pregunta_dict["respuesta_correcta"] = respuesta

        preguntas.append(pregunta_dict)

    # Seleccionar una pregunta aleatoria
    seleccionada = random.choice(preguntas)
    return seleccionada
def escoger_pregunta_aleatoria_10_16(
    file_path: str | Path = "resources\mru_question_bank.json",
    n_each: int = 2,
    seed: int | None = None
):
    if seed is not None:
        random.seed(seed)

    # Leer banco de preguntas
    with open(file_path, encoding="utf-8") as f:
        bank = json.load(f)

    # Clasificar por tipo
    by_type = {"conceptual": [], "calculo": [], "grafico": []}
    for question in bank:
        qtype = question["type"]
        if qtype in by_type:
            by_type[qtype].append(question)

    # Elegir n_each al azar de cada categoría
    selected = []
    for qtype, bucket in by_type.items():
        if len(bucket) < n_each:
            raise ValueError(f"No hay suficientes preguntas tipo '{qtype}'.")
        selected.extend(random.sample(bucket, k=n_each))

    # Mezclar el resultado final para que no queden agrupadas por tipo
    random.shuffle(selected)
    return selected