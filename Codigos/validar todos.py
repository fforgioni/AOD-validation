# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:44:46 2024

@author: ferfo
"""

import xarray as xr
import numpy as np
import os
import pandas as pd

def calculate_metrics(data1, data2):
    # Asegúrate de que las dimensiones coinciden
    assert data1.shape == data2.shape, "Las dimensiones de los datos no coinciden"
    
    # Correlación
    corr = np.corrcoef(data1.flatten(), data2.flatten())[0, 1]
    
    # RMSE
    rmse = np.sqrt(np.mean((data1 - data2) ** 2))
    
    # MBE
    mbe = np.mean(data1 - data2)
    
    return corr, rmse, mbe

def process_files(reference_file, input_folder, var_name1, var_name2, output_csv):
    # Cargar el archivo de referencia
    ref_ds = xr.open_dataset(reference_file)
    ref_data = ref_ds[var_name1].values

    # Lista para almacenar los resultados
    results = []

    # Recorrer todos los archivos .nc en el directorio de entrada
    for file in os.listdir(input_folder):
        if file.endswith(".nc"):
            file_path = os.path.join(input_folder, file)
            # Cargar el archivo actual
            ds = xr.open_dataset(file_path)
            data = ds[var_name2].values

            # Calcular las métricas
            corr, rmse, mbe = calculate_metrics(ref_data, data)

            # Guardar los resultados
            results.append({
                "archivo": file,
                "correlacion": corr,
                "rmse": rmse,
                "mbe": mbe
            })

            # Cerrar el dataset
            ds.close()
    
    # Cerrar el dataset de referencia
    ref_ds.close()

    # Convertir los resultados en un DataFrame de pandas
    df = pd.DataFrame(results)
    
    # Guardar los resultados en un archivo CSV
    df.to_csv(output_csv, index=False)
    print(f"Resultados guardados en {output_csv}")

# Especifica las rutas de los archivos y el nombre de las variables a comparar
reference_file = 'C:/Users/ferfo/OneDrive/Desktop/merraorg.nc'
input_folder = 'C:/Users/ferfo/OneDrive/Desktop/aerosol org aso'
var_name1 = 'OCEXTTAU'
var_name2 = 'od550oa'
output_csv = 'C:/Users/ferfo/OneDrive/Desktop/resultados_merra.csv'

# Ejecutar la función para procesar los archivos
process_files(reference_file, input_folder, var_name1, var_name2, output_csv)
