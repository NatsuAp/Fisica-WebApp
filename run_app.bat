@echo off
setlocal

:: Ruta al entorno virtual (ajusta si es diferente)
set VENV_DIR=.venv
set APP_FILE=app.py

:: Verificar que el entorno virtual existe
if not exist %VENV_DIR%\Scripts\activate (
    echo El entorno virtual no existe en "%VENV_DIR%".
    echo Por favor crea uno con: python -m venv %VENV_DIR%
    exit /b 1
)

:: Activar el entorno virtual
call %VENV_DIR%\Scripts\activate

:: Instalar o actualizar dependencias si existe requirements.txt


:: Verificar que el archivo de la app exista
if not exist %APP_FILE% (
    echo No se encontró el archivo %APP_FILE%.
    exit /b 1
)

:: Ejecutar la app de Streamlit
echo Ejecutando Streamlit...
streamlit run %APP_FILE%

endlocal
