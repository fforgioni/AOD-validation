# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:38:10 2024

@author: ferfo
"""

import os
import pandas as pd
import re

# Ruta de la carpeta que contiene los archivos CSV
folder_path = 'C:/Users/ferfo/OneDrive/Desktop/aeronet'
output_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/resultados_aerosol.xlsx'

# Columnas que queremos mantener
columnas_requeridas = ['Date(dd:mm:yyyy)', 'Time(hh:mm:ss)', 'Day_of_Year', 'Day_of_Year(Fraction)', 'AOD_500nm', '440-870_Angstrom_Exponent']

# Crear un diccionario para almacenar los DataFrames
dfs = {}

# Función para limpiar el nombre de la estación eliminando números
def limpiar_nombre_estacion(nombre):
    return re.sub(r'\d+', '', nombre).strip()

# Iterar sobre cada archivo CSV en la carpeta
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # Leer el DataFrame del archivo CSV actual
        file_path = os.path.join(folder_path, file_name)
        
        try:
            df = pd.read_csv(file_path, encoding='latin1')  # Intentar con la codificación 'latin1'
            
            # Verificar las columnas presentes en el DataFrame
            columnas_presentes = df.columns.tolist()
            print(f"Columnas en el archivo {file_name}: {columnas_presentes}")
            
            # Filtrar solo las columnas requeridas
            df_filtrado = df[columnas_requeridas]
            
            # Extraer el nombre de la estación del nombre del archivo
            nombre_estacion_completo = os.path.splitext(file_name)[0]
            nombre_estacion = limpiar_nombre_estacion(nombre_estacion_completo)
            
            # Asegurarse de que el nombre de la hoja no exceda los 31 caracteres
            nombre_estacion = nombre_estacion[:31]
            
            # Añadir el DataFrame al diccionario, usando el nombre de la estación como la clave
            dfs[nombre_estacion] = df_filtrado
            
        except Exception as e:
            print(f"Error al procesar el archivo {file_name}: {e}")

# Guardar todos los DataFrames en un solo archivo Excel, cada uno en una hoja diferente
with pd.ExcelWriter(output_excel_path) as writer:
    for nombre_estacion, df in dfs.items():
        # Asegurarse de que el nombre de la hoja sea único
        sheet_name = nombre_estacion
        counter = 1
        while sheet_name in writer.sheets:
            sheet_name = f"{nombre_estacion[:28]}_{counter}"
            counter += 1
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Todos los datos han sido procesados y guardados en '{output_excel_path}'")
