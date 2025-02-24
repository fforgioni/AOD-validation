# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:03:54 2024

@author: ferfo
"""

import pandas as pd
import json

# Leer el archivo JSON fusionado línea por línea
data = []
with open('C:/Users/ferfo/OneDrive/Desktop/incendios_sudamerica.json', 'r') as file:
    for line in file:
        data.append(json.loads(line))

# Convertir la lista de diccionarios a un DataFrame de pandas
df = pd.DataFrame(data)

# Seleccionar las columnas deseadas
columnas_deseadas = ['latitude', 'longitude', 'acq_date', 'instrument', 'type', 'confidence']
df_filtrado = df[columnas_deseadas]

# Filtrar los datos según las condiciones especificadas
df_filtrado = df_filtrado[(df_filtrado['type'] == 0) & (df_filtrado['confidence'] >= 80)]

# Guardar el DataFrame filtrado en un nuevo archivo JSON
df_filtrado.to_json('archivo_filtrado.json', orient='records', lines=True)

print("Datos filtrados y guardados en archivo_filtrado.json exitosamente.")
