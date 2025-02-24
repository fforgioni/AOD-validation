# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:13:43 2024

@author: ferfo
"""

import pandas as pd

# Ruta del archivo Excel
input_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/resultados_aerosol.xlsx'
output_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/resultados_aerosol_modificado.xlsx'

# Leer el archivo Excel
excel_data = pd.ExcelFile(input_excel_path)

# Crear un diccionario para almacenar los DataFrames modificados
dfs_modificados = {}

# Iterar sobre cada hoja en el archivo Excel
for sheet_name in excel_data.sheet_names:
    df = pd.read_excel(input_excel_path, sheet_name=sheet_name)
    
    # Verificar si la columna 'Date(dd:mm:yyyy)' está presente
    if 'Date(dd:mm:yyyy)' in df.columns:
        # Separar la columna 'Date(dd:mm:yyyy)' en día, mes y año
        fecha_separada = df['Date(dd:mm:yyyy)'].str.split(':', expand=True)
        fecha_separada.columns = ['Dia', 'Mes', 'Año']
        
        # Insertar las nuevas columnas después de 'Date(dd:mm:yyyy)'
        df.insert(1, 'Dia', fecha_separada['Dia'])
        df.insert(2, 'Mes', fecha_separada['Mes'])
        df.insert(3, 'Año', fecha_separada['Año'])
        
        # Agregar el DataFrame modificado al diccionario
        dfs_modificados[sheet_name] = df

# Guardar todos los DataFrames modificados en un nuevo archivo Excel
with pd.ExcelWriter(output_excel_path) as writer:
    for sheet_name, df in dfs_modificados.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Todos los datos han sido procesados y guardados en '{output_excel_path}'")
