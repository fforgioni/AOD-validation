# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:46:15 2024

@author: ferfo
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import netCDF4 as nc
import numpy as np
from matplotlib.colors import BoundaryNorm, ListedColormap

# Leer los datos de los archivos NetCDF
file_cams = 'C:/Users/ferfo/OneDrive/Desktop/a/camsorg.nc'
ds_cams = nc.Dataset(file_cams)

# Asumimos que los datos de AOD están en la variable 'omaod550' en el archivo CAMS
aod_cams = ds_cams.variables['omaod550'][:]

# Coordenadas
lats = ds_cams.variables['latitude'][:]
lons = ds_cams.variables['longitude'][:]

# Crear una lista de colores y un normalizador para la barra de colores discretizada
cmap = plt.get_cmap('gist_heat_r')
colors = cmap(np.linspace(0, 1, cmap.N))

# Crear el nuevo colormap sin cambiar ningún color a blanco
new_cmap = ListedColormap(colors)

bounds = np.arange(0,  1.1, 0.05)
norm = BoundaryNorm(bounds, ncolors=new_cmap.N, clip=True)

# Configuración de los subplots
fig1, axes1 = plt.subplots(nrows=3, ncols=4, figsize=(20, 15), subplot_kw={'projection': ccrs.PlateCarree()})
fig1.subplots_adjust(wspace=-0.6, hspace=0.3)  # Ajustar el espaciado entre subplots

# Títulos de los subplots
meses = ['CAMS. Enero', 'CAMS. Febrero', 'CAMS. Marzo', 'CAMS. Abril', 'CAMS. Mayo', 'CAMS. Junio', 'CAMS. Julio', 'CAMS. Agosto', 'CAMS. Septiembre', 'CAMS. Octubre', 'CAMS. Noviembre', 'CAMS. Diciembre']

# Plotear los datos de CAMS
for i, ax in enumerate(axes1.flat):
    pcm = ax.pcolormesh(lons, lats, aod_cams[i, :, :], transform=ccrs.PlateCarree(), cmap=new_cmap, norm=norm)
    ax.coastlines()
    ax.set_extent([-81, -34, -56, 10], crs=ccrs.PlateCarree())  # Establecer límites para Sudamérica
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.OCEAN, zorder=100, edgecolor='k')
    ax.set_title(meses[i], fontsize=18)  # Ajustar el tamaño de fuente de los títulos

# Añadir la barra de colores al lado derecho de los subplots
cbar_ax = fig1.add_axes([0.8, 0.13, 0.02, 0.75])  # [left, bottom, width, height]
cbar = fig1.colorbar(pcm, cax=cbar_ax, boundaries=bounds, ticks=bounds)
cbar.ax.set_yticklabels([f'{x:.3f}' for x in bounds], fontsize=16)   # Formatear los ticks y ajustar el tamaño de fuente
cbar.set_label('Aerosoles organicos 550nm', fontsize=16, labelpad=20)  # Añadir una leyenda a la barra de colores con separación

# Guardar la figura
plt.savefig('C:/Users/ferfo/OneDrive/Desktop/orgcams.png', dpi=300, bbox_inches='tight')

plt.show()