# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:05:12 2024

@author: ferfo
"""

import xarray as xr
import numpy as np

def compare_nc_coordinates(file1, file2):
    try:
        dataset1 = xr.open_dataset(file1)
        dataset2 = xr.open_dataset(file2)

        if 'latitude' in dataset1 and 'longitude' in dataset1:
            latitudes1 = dataset1['latitude'].values
            longitudes1 = dataset1['longitude'].values
        elif 'lat' in dataset1 and 'lon' in dataset1:
            latitudes1 = dataset1['lat'].values
            longitudes1 = dataset1['lon'].values
        else:
            print("No se encontraron variables de coordenadas en el primer archivo.")
            return

        if 'latitude' in dataset2 and 'longitude' in dataset2:
            latitudes2 = dataset2['latitude'].values
            longitudes2 = dataset2['longitude'].values
        elif 'lat' in dataset2 and 'lon' in dataset2:
            latitudes2 = dataset2['lat'].values
            longitudes2 = dataset2['lon'].values
        else:
            print("No se encontraron variables de coordenadas en el segundo archivo.")
            return

        latitudes_match = np.array_equal(latitudes1, latitudes2)
        longitudes_match = np.array_equal(longitudes1, longitudes2)

        if latitudes_match and longitudes_match:
            print("Las coordenadas de los dos archivos coinciden.")
        else:
            print("Las coordenadas de los dos archivos no coinciden.")
            if not latitudes_match:
                print("Las latitudes no coinciden.")
            if not longitudes_match:
                print("Las longitudes no coinciden.")

    except Exception as e:
        print(f"Ocurrió un error al leer los archivos: {e}")

# Rutas de los archivos
file1 = 'C:/Users/ferfo/OneDrive/Desktop/camsbc2.nc'
file2 = 'C:/Users/ferfo/OneDrive/Desktop/od550bc_AERmon_CNRM-CM6-1_historical_cropped.nc'

# Comparar coordenadas de ambos archivos
compare_nc_coordinates(file1, file2)
