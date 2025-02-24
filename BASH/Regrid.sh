#!/bin/bash

# Definir las rutas de las carpetas de entrada y salida
input_folder="/mnt/c/Users/ferfo/OneDrive/desktop/ensamble"
output_folder="/mnt/c/Users/ferfo/OneDrive/desktop/grilla"

# Crear la carpeta de salida si no existe
mkdir -p "$output_folder"

# Definir el archivo de la rejilla
grid_file="grid_0.75x0.75.txt"

# Crear el archivo de definición de la rejilla
cat <<EOL > "$grid_file"
gridtype = lonlat
xsize    = 480
ysize    = 240
xfirst   = 0.0
xinc     = 0.75
yfirst   = -89.625
yinc     = 0.75
EOL

# Procesar cada archivo en la carpeta de entrada
for input_file in "$input_folder"/*.nc; do
  # Obtener el nombre del archivo sin la ruta
  filename=$(basename "$input_file")
  # Definir el archivo de salida
  output_file="$output_folder/$filename"
  # Aplicar el comando CDO
  cdo remapbil,"$grid_file" "$input_file" "$output_file"
  echo "Procesado $input_file -> $output_file"
done

echo "Todos los archivos han sido procesados."
