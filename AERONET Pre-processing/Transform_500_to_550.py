# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:38:09 2024

@author: ferfo
"""

import pandas as pd

# Leer el archivo Excel con todas las hojas
input_excel_path = "C:/Users/ferfo/OneDrive/Desktop/nuevo_archivo_completo.xlsx"
excel_file = pd.ExcelFile(input_excel_path)

# Crear un diccionario para almacenar los DataFrames
dfs = {}

# Iterar sobre cada hoja del archivo Excel
for sheet_name in excel_file.sheet_names:
    # Leer el DataFrame de la hoja actual
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Verificar si las columnas necesarias existen en el DataFrame
    if 'AOD_500nm' in df.columns and '440-870_Angstrom_Exponent' in df.columns:
        # Calcular AOD550nm
        df['AOD550nm'] = df['AOD_500nm'] * (550 / 500) ** (-df['440-870_Angstrom_Exponent'])
    else:
        print(f"Columnas necesarias no encontradas en la hoja '{sheet_name}'")

    # Guardar el DataFrame en el diccionario
    dfs[sheet_name] = df

# Guardar todos los DataFrames en un solo archivo Excel, cada uno en una hoja diferente
output_excel_path = "C:/Users/ferfo/OneDrive/Desktop/nuevo_archivo_completo_con_AOD550nm.xlsx"
with pd.ExcelWriter(output_excel_path) as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Todos los datos han sido procesados y guardados en '{output_excel_path}'")
