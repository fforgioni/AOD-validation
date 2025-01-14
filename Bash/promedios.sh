#!/bin/bash

# Directorios
input_dir="/mnt/c/Users/ferfo/OneDrive/Desktop/grafico"
output_dir="/mnt/c/Users/ferfo/OneDrive/Desktop/listos"

# Crear el directorio de salida si no existe
mkdir -p "$output_dir"

# Procesar cada archivo .nc en el directorio de entrada
for input_file in "$input_dir"/*.nc; do
    # Obtener el nombre del archivo sin la ruta
    filename=$(basename "$input_file")
    
    # Definir el archivo de salida
    output_file="$output_dir/$filename"
    
    # Aplicar el comando CDO para calcular el promedio mensual climatológico
    cdo ymonmean "$input_file" "$output_file"
    
    echo "Procesado: $input_file -> $output_file"
done

echo "Todos los archivos han sido procesados."
