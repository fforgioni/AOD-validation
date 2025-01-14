#!/bin/bash

# Directorios de entrada y salida
input_dir="/mnt/c/Users/ferfo/OneDrive/Desktop/terminado1"
output_dir="/mnt/c/Users/ferfo/OneDrive/Desktop/b"

# Crear el directorio de salida si no existe
mkdir -p "$output_dir"

# Loop para procesar todos los archivos .nc en el directorio de entrada
for file in "$input_dir"/*.nc; do
  # Obtener el nombre del archivo sin la ruta
  filename=$(basename "$file")

  # Usar CDO para seleccionar el rango de fechas deseado
  cdo seldate,2003-01-01,2014-12-31 "$file" "$output_dir/$filename"
done

