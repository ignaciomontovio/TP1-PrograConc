#!/usr/bin/env bash
SLEEP_TIME=5

echo "Compilando..."
g++ -std=c++17 -g src/process_tree.cpp -o bin/process_tree
if [ $? -ne 0 ]; then
    echo "Compilacion fallida."
    exit 1
fi

echo "Ejecutando..."
bin/process_tree $SLEEP_TIME 1>output 2>/dev/null &
FIRST_PROCESS=$!

sleep 1 # Esperamos un segundo a que se creen los nodos...
echo "Arbol de procesos:"
pstree -pc $FIRST_PROCESS

wait $FIRST_PROCESS # Esperamos a que se cierren...

if [ $? -eq 0 ]; then
    echo -e "\nSalida del programa:"
    cat ./output
else
    echo "Proceso termino incorrectamente."
    exit 1
fi