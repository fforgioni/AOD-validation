# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:38:56 2024

@author: ferfo
"""

import pandas as pd
import os

# Ruta del archivo Excel de entrada
input_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/resultados_aerosol_modificado.xlsx'
temp_folder_path = 'C:/Users/ferfo/OneDrive/Desktop/temp_sheets'

# Crear una carpeta para las hojas procesadas
os.makedirs(temp_folder_path, exist_ok=True)

# Leer el archivo Excel con todas las hojas
excel_file = pd.ExcelFile(input_excel_path, engine='openpyxl')

# Iterar sobre cada hoja del archivo Excel
for sheet_name in excel_file.sheet_names:
    try:
        # Leer el DataFrame de la hoja actual
        df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')

        # Calcular la fecha máxima en el DataFrame
        fecha_maxima = pd.to_datetime(df[['Año', 'Mes', 'Dia']].astype(str).agg('-'.join, axis=1)).max()

        # Crear un rango de fechas desde el 01/01/2001 hasta la fecha máxima en tu DataFrame
        fechas_faltantes = pd.date_range(start="2003-01-01", end="2023-12-30")

        # Convertir las fechas a DataFrame
        df_fechas_faltantes = pd.DataFrame({'Fecha': fechas_faltantes})

        # Separar las fechas en columnas de día, mes y año
        df_fechas_faltantes['Dia'] = df_fechas_faltantes['Fecha'].dt.day
        df_fechas_faltantes['Mes'] = df_fechas_faltantes['Fecha'].dt.month
        df_fechas_faltantes['Año'] = df_fechas_faltantes['Fecha'].dt.year

        # Fusionar los DataFrames para completar los datos faltantes
        df_completo = pd.merge(df_fechas_faltantes, df, on=['Dia', 'Mes', 'Año'], how='left')

        # Ordenar el DataFrame completo por fecha
        df_completo = df_completo.sort_values(by='Fecha').reset_index(drop=True)

        # Guardar el DataFrame completo en un archivo separado
        output_file_path = os.path.join(temp_folder_path, f"{sheet_name}.xlsx")
        df_completo.to_excel(output_file_path, index=False)
    except Exception as e:
        print(f"Error al procesar la hoja {sheet_name}: {e}")

print(f"Las hojas procesadas se han guardado en la carpeta '{temp_folder_path}'")

# Ruta de la carpeta con los archivos procesados
temp_folder_path = 'C:/Users/ferfo/OneDrive/Desktop/temp_sheets'
output_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/nuevo_archivo_completo.xlsx'

# Crear un escritor de Excel para el archivo final
with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
    # Iterar sobre cada archivo procesado y combinar en un solo archivo Excel
    for temp_file in os.listdir(temp_folder_path):
        sheet_name = os.path.splitext(temp_file)[0]
        temp_file_path = os.path.join(temp_folder_path, temp_file)
        df_temp = pd.read_excel(temp_file_path, engine='openpyxl')
        df_temp.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Todos los datos han sido procesados y guardados en '{output_excel_path}'")

