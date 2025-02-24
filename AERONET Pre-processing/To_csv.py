# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:39:23 2024

@author: ferfo
"""

import os
import pandas as pd

# Ruta de la carpeta que contiene los archivos
folder_path = 'C:/Users/ferfo/OneDrive/Desktop/aeronet'

# Función para extraer el nombre completo de la estación del nombre del archivo
def get_station_name(file_name):
    return os.path.splitext(file_name)[0]

# Lista para almacenar los nombres de los archivos
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for file_name in file_list:
    try:
        # Leer el archivo
        file_path = os.path.join(folder_path, file_name)
        data = pd.read_csv(file_path, skiprows=6, encoding='latin1')  # Ajustar skiprows y encoding según sea necesario
        
        # Extraer el nombre completo de la estación
        station_name = get_station_name(file_name)
        
        # Crear el nombre del archivo CSV
        csv_file_name = f"{station_name}.csv"
        csv_file_path = os.path.join(folder_path, csv_file_name)
        
        # Guardar el archivo CSV
        data.to_csv(csv_file_path, index=False)
        print(f"Archivo guardado: {csv_file_name}")
    except Exception as e:
        print(f"Error al procesar el archivo {file_name}: {e}")
