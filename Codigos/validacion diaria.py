# -*- coding: utf-8 -*-
"""
Created on Wed May 29 17:22:51 2024

@author: ferfo
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from scipy.stats import pearsonr

# Función para calcular BIAS
def calculate_bias(observations, predictions):
    return np.mean(predictions - observations)

# Función para calcular RMSE
def calculate_rmse(observations, predictions):
    return np.sqrt(mean_squared_error(observations, predictions))

# Función para calcular el coeficiente de correlación
def calculate_correlation(observations, predictions):
    return pearsonr(observations, predictions)[0]

# Leer el archivo Excel con los datos
input_excel_path = 'C:/Users/ferfo/OneDrive/Desktop/diario.xlsx'
df = pd.read_excel(input_excel_path, sheet_name=None)  # Leer todas las hojas

# Crear listas para almacenar los resultados
resultados_merra = []
resultados_cams = []

# Iterar sobre cada hoja (estación)
for sheet_name, data in df.items():
    # Asegurarse de que las columnas necesarias existan
    if 'Fecha' in data.columns and 'aeronet' in data.columns and 'merra' in data.columns and 'cams' in data.columns:
        # Filtrar valores mayores que 5
        data = data[(data['aeronet'] <= 5) & (data['merra'] <= 5) & (data['cams'] <= 5)]
        
        # Drop rows where 'aeronet' is NaN to ensure same length comparison
        data = data.dropna(subset=['aeronet'])
        data_cams = data.dropna(subset=['cams'])
        data_merra = data.dropna(subset=['merra'])

        # Calcular las métricas para CAMS
        if not data_cams.empty:
            corr_cams = calculate_correlation(data_cams['aeronet'], data_cams['cams'])
            rmse_cams = calculate_rmse(data_cams['aeronet'], data_cams['cams'])
            bias_cams = calculate_bias(data_cams['aeronet'], data_cams['cams'])
            resultados_cams.append({'Estacion': sheet_name, 'Correlacion': corr_cams, 'RMSE': rmse_cams, 'BIAS': bias_cams})

        # Calcular las métricas para MERRA
        if not data_merra.empty:
            corr_merra = calculate_correlation(data_merra['aeronet'], data_merra['merra'])
            rmse_merra = calculate_rmse(data_merra['aeronet'], data_merra['merra'])
            bias_merra = calculate_bias(data_merra['aeronet'], data_merra['merra'])
            resultados_merra.append({'Estacion': sheet_name, 'Correlacion': corr_merra, 'RMSE': rmse_merra, 'BIAS': bias_merra})
    else:
        print(f"Las columnas necesarias no se encontraron en la hoja '{sheet_name}'")

# Convertir los resultados en DataFrames
df_resultados_cams = pd.DataFrame(resultados_cams)
df_resultados_merra = pd.DataFrame(resultados_merra)

# Guardar los resultados en archivos Excel
df_resultados_cams_path = 'C:/Users/ferfo/OneDrive/Desktop/resultados_cams_diario.xlsx'
df_resultados_merra_path = 'C:/Users/ferfo/OneDrive/Desktop/resultados_merra_diario.xlsx'

df_resultados_cams.to_excel(df_resultados_cams_path, index=False)
df_resultados_merra.to_excel(df_resultados_merra_path, index=False)

print("Resultados de CAMS y MERRA han sido calculados y guardados.")

