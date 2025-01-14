#!/bin/bash

# Definir las rutas de las carpetas de entrada y salida
input_folder="/mnt/c/Users/ferfo/OneDrive/desktop/grilla"
output_folder="/mnt/c/Users/ferfo/OneDrive/desktop/recorte"

# Definir límites de coordenadas
lon_min=-82
lon_max=-34
lat_min=-56
lat_max=13

# Crear directorio de salida si no existe
mkdir -p $output_folder

# Recorrer todos los archivos .nc en el directorio de entrada
for file in $input_folder/*.nc; do
  # Obtener el nombre del archivo sin la ruta
  filename=$(basename "$file")
  
  # Definir el nombre del archivo de salida
  output_file="$output_folder/${filename%.nc}_cropped.nc"
  
  # Aplicar el recorte con CDO
  cdo sellonlatbox,$lon_min,$lon_max,$lat_min,$lat_max "$file" "$output_file"
  
  echo "Archivo $filename recortado y guardado en $output_file"
done

echo "Todos los archivos han sido recortados."
