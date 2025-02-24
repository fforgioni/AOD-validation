#!/bin/bash

# Definir las rutas de las carpetas de entrada y salida
input_folder="/mnt/c/Users/ferfo/OneDrive/desktop/recorte"
output_folder="/mnt/c/Users/ferfo/OneDrive/desktop/limpio"

# Crear la carpeta de salida si no existe
mkdir -p "$output_folder"

# Iterar sobre todos los archivos en la carpeta de entrada
for file in "$input_folder"/*; do
  # Obtener el nombre del archivo sin la ruta
  filename=$(basename "$file")

  # Remover las frases específicas del nombre del archivo
  new_filename=${filename//od550aer_AERmon_/}
  new_filename=${new_filename//_historical_mean_cropped_ASO/}

  # Copiar el archivo al directorio de salida con el nuevo nombre
  cp "$file" "$output_folder/$new_filename"
done

echo "Archivos renombrados y copiados a $output_folder"
