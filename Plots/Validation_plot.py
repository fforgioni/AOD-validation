# -*- coding: utf-8 -*-
"""
Created on Thu May 30 00:13:02 2024

@author: ferfo
"""

import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from matplotlib.colors import BoundaryNorm

# Configurar la fuente a Arial
plt.rc('font', family='Arial')

# Cargar los datos desde el archivo Excel
file_path = 'C:/Users/ferfo/OneDrive/Escritorio/metricas-mensuales.xlsx'
merra_data = pd.read_excel(file_path, sheet_name='Merra')
cams_data = pd.read_excel(file_path, sheet_name='Cams')

# Extraer los datos necesarios de ambas hojas
def extract_data(data):
    latitudes = data['latitud']
    longitudes = data['longitud']
    correlacion = data['Correlacion']
    rmse = data['RMSE']
    bias = data['BIAS']
    return latitudes, longitudes, correlacion, rmse, bias

merra_lat, merra_lon, merra_cor, merra_rmse, merra_bias = extract_data(merra_data)
cams_lat, cams_lon, cams_cor, cams_rmse, cams_bias = extract_data(cams_data)

# Crear figura y subplots
fig, axs = plt.subplots(2, 3, figsize=(25, 15), subplot_kw={'projection': ccrs.PlateCarree()})

# Configuración general para cada subplot
def setup_map(ax):
    ax.set_extent([-90, -30, -60, 15], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, zorder=0)
    ax.add_feature(cfeature.OCEAN, zorder=0)
    ax.add_feature(cfeature.COASTLINE, zorder=1)
    ax.add_feature(cfeature.BORDERS, linestyle='-', zorder=1)

# Definir un tamaño fijo para todas las pelotitas
fixed_size = 100

# Crear subplots para MERRA y CAMS
metrics_merra = [merra_cor, merra_rmse, merra_bias]
metrics_cams = [cams_cor, cams_rmse, cams_bias]
titles = ['Correlación', 'RMSE', 'BIAS']
cmaps = ['Spectral', 'viridis', 'coolwarm']
clims = [(0, 1), (0, 0.2), (-0.2, 0.2)]
ticks = [
    [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], 
    [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2], 
    [-0.2, -0.16, -0.12, -0.08, -0.04, 0, 0.04, 0.08, 0.12, 0.16, 0.2]
]

# Títulos personalizados para cada subplot
subplot_titles = [
    '(a)',
    '(c)',
    '(e)',
    '(b)',
    '(d)',
    '(f)'
]

# Crear subplots y colorbars
for i, (metric_merra, metric_cams, title, cmap, clim, tick) in enumerate(zip(metrics_merra, metrics_cams, titles, cmaps, clims, ticks)):
    # Crear un colormap discreto
    cmap = plt.get_cmap(cmap)
    norm = BoundaryNorm(boundaries=tick, ncolors=cmap.N, clip=True)

    # Subplot MERRA
    ax = axs[0, i]
    setup_map(ax)
    scatter_merra = ax.scatter(
        merra_lon, merra_lat, c=metric_merra, cmap=cmap, norm=norm, 
        s=fixed_size, edgecolor='k', transform=ccrs.PlateCarree()
    )
    ax.set_title(subplot_titles[i], fontsize=22)  # Título personalizado
    
    # Subplot CAMS
    ax = axs[1, i]
    setup_map(ax)
    scatter_cams = ax.scatter(
        cams_lon, cams_lat, c=metric_cams, cmap=cmap, norm=norm, 
        s=fixed_size, edgecolor='k', transform=ccrs.PlateCarree()
    )
    ax.set_title(subplot_titles[i + 3], fontsize=22)  # Título personalizado
    
    # Colorbar compartida
    cbar = fig.colorbar(scatter_merra, ax=axs[:, i], orientation='vertical', pad=0.02, aspect=30)
    cbar.set_ticks(tick)
    cbar.set_ticklabels([f'{x:.2f}' for x in tick])
    cbar.ax.tick_params(labelsize=20)  # Tamaño de los ticks

    # Ajustar la posición manualmente
    if i == 0:
        cbar.ax.set_position([0.4, 0.05, 0.02, 0.85])  # Colorbar del primer subplot
    elif i == 1:
        cbar.ax.set_position([0.7, 0.05, 0.02, 0.85])  # Colorbar del segundo subplot
    elif i == 2:
        cbar.ax.set_position([1.01, 0.05, 0.02, 0.85])  # Colorbar del tercer subplot

# Título general de la figura
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Guardar la figura
fig.savefig('C:/Users/ferfo/OneDrive/Escritorio/Fig-4.png', dpi=300, bbox_inches='tight')

plt.show()


