# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:40:18 2024

@author: ferfo
"""

import pandas as pd

# Leer el archivo Excel con todas las hojas
input_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/nuevo_archivo_completo_con_AOD550nm.xlsx'
excel_file = pd.ExcelFile(input_excel_path)

# Crear un diccionario para almacenar los DataFrames procesados
resultados = {}

# Iterar sobre cada hoja del archivo Excel
for sheet_name in excel_file.sheet_names:
    # Leer el DataFrame de la hoja actual
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Verificar que las columnas 'Dia', 'Mes' y 'Año' existen
    if all(col in df.columns for col in ['Dia', 'Mes', 'Año']):
        # Renombrar temporalmente las columnas para usar pd.to_datetime
        df.rename(columns={'Dia': 'day', 'Mes': 'month', 'Año': 'year'}, inplace=True)

        # Crear la columna 'Fecha' a partir de las columnas 'day', 'month' y 'year'
        df['Fecha'] = pd.to_datetime(df[['year', 'month', 'day']])

        # Revertir los nombres de las columnas
        df.rename(columns={'day': 'Dia', 'month': 'Mes', 'year': 'Año'}, inplace=True)
        
        # Reemplazar los valores negativos en 'AOD_500nm' por NaN
        df['AOD550nm'] = df['AOD550nm'].apply(lambda x: x if x >= 0 else None)

        # Calcular el promedio de AOD_500nm por día
        promedio_por_dia = df.groupby('Fecha')['AOD550nm'].mean().reset_index()

        # Guardar el DataFrame procesado en el diccionario
        resultados[sheet_name] = promedio_por_dia
    else:
        print(f"Las columnas necesarias 'Dia', 'Mes' y 'Año' no se encontraron en la hoja '{sheet_name}'")

# Guardar todos los DataFrames en un solo archivo Excel, cada uno en una hoja diferente
output_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/promedio_aod.xlsx'
with pd.ExcelWriter(output_excel_path) as writer:
    for sheet_name, df in resultados.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Promedio diario de AOD-500nm calculado y guardado en 'promedio_aod.xlsx'")
