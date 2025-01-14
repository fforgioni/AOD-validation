#!/bin/bash

# Directorios de entrada y salida
input_folder="/mnt/c/Users/ferfo/OneDrive/desktop/recorte"
output_folder="/mnt/c/Users/ferfo/OneDrive/desktop/aso"

# Crear la carpeta de destino si no existe
mkdir -p "$output_folder"

# Iterar sobre todos los archivos .nc en la carpeta de entrada
for file in "$input_folder"/*.nc; do
    # Obtener el nombre del archivo sin la ruta y la extensión
    filename=$(basename -- "$file")
    
    # Generar el nombre del archivo de salida
    outfile="$output_folder/${filename%.nc}_ASO.nc"
    
    # Seleccionar los meses de agosto, septiembre y octubre
    cdo selmon,8,9,10 "$file" "$outfile"
done

echo "Proceso completado. Los archivos seleccionados se han guardado en la carpeta 'aso'."
