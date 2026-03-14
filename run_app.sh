#!/bin/bash

CONTAINER_NAME="fisica_app"

cleanup() {
    echo "Cerrando contenedor..."
    docker stop $CONTAINER_NAME 2>/dev/null
}

trap cleanup EXIT INT TERM HUP

echo "Ejecutando Streamlit..."

docker rm -f $CONTAINER_NAME 2>/dev/null

docker run --name $CONTAINER_NAME -p 8501:8501 fisica_app &
DOCKER_PID=$!

sleep 3

if command -v xdg-open > /dev/null; then
    xdg-open http://localhost:8501
elif command -v open > /dev/null; then
    open http://localhost:8501
else
    echo "Abre manualmente: http://localhost:8501"
fi

wait $DOCKER_PID
