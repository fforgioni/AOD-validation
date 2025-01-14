# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:46:46 2024

@author: ferfo
"""

import xarray as xr
import os
import cftime

def convert_time_to_noleap(ds):
    """Convierte la variable de tiempo a calendario 'noleap'"""
    time = ds['time']
    noleap_time = xr.cftime_range(start=cftime.DatetimeNoLeap(time.dt.year[0], time.dt.month[0], time.dt.day[0], time.dt.hour[0]), 
                                  periods=len(time), 
                                  freq='MS')
    ds['time'] = noleap_time
    return ds

def ensemble_models(input_folder, var_name, output_file):
    # Lista para almacenar los datasets
    datasets = []

    # Recorrer todos los archivos .nc en el directorio de entrada
    for file in os.listdir(input_folder):
        if file.endswith(".nc"):
            file_path = os.path.join(input_folder, file)
            # Cargar el archivo actual
            ds = xr.open_dataset(file_path)

            # Convertir el calendario a 'noleap' para evitar conflictos
            ds = convert_time_to_noleap(ds)
            
            datasets.append(ds[var_name])
    
    # Crear un ensamblaje de los modelos (calcular el promedio)
    ensemble = xr.concat(datasets, dim='model').mean(dim='model')

    # Guardar el ensamblaje en un archivo NetCDF
    ensemble.to_netcdf(output_file)
    print(f"Ensamblaje guardado en {output_file}")

# Especifica la carpeta de entrada y el archivo de salida
input_folder = 'C:/Users/ferfo/OneDrive/Desktop/orgaso'
var_name = 'od550oa'
output_file = 'C:/Users/ferfo/OneDrive/Desktop/ensembleorgaso.nc'

# Ejecutar la función para crear el ensamblaje
ensemble_models(input_folder, var_name, output_file)
