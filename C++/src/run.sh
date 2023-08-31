#!/usr/bin/env bash
SLEEP_TIME=5

echo "Compilando..."
g++ -std=c++17 -g src/process_tree.cpp -o bin/process_tree

echo "Ejecutando..."
bin/process_tree $SLEEP_TIME 1>output 2>/dev/null &
FIRST_PROCESS=$!

sleep 1 # Esperamos un segundo a que se creen los nodos...
echo "Arbol de procesos:"
pstree -pc $FIRST_PROCESS

sleep $(expr $SLEEP_TIME + 1) # Esperamos a que se cierren...

echo -e "\nSalida del programa:"
cat ./output