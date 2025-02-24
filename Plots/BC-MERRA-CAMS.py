# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:48:27 2025

@author: ferfo
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import netCDF4 as nc
import numpy as np
from matplotlib.colors import BoundaryNorm, ListedColormap

# Leer los datos de los archivos NetCDF
file_cams = 'C:/Users/ferfo/OneDrive/Escritorio/a/camsbc.nc'
file_merra = 'C:/Users/ferfo/OneDrive/Escritorio/a/merrabc.nc'

ds_cams = nc.Dataset(file_cams)
ds_merra = nc.Dataset(file_merra)

# Extraer los datos de AOD y coordenadas
aod_cams = ds_cams.variables['bcaod550'][:]
aod_merra = ds_merra.variables['TOTEXTTAU_regridded'][:]

lats = ds_cams.variables['latitude'][:]
lons = ds_cams.variables['longitude'][:]

# Crear colormap personalizado con valores de 0 en blanco
cmap_base = plt.get_cmap('copper_r')
colors = cmap_base(np.linspace(0, 1, cmap_base.N))
colors[0] = [1, 1, 1, 1]  # Hacer el primer color (cero) blanco
cmap_custom = ListedColormap(colors)

bounds = np.arange(0, 0.181, 0.02)
norm = BoundaryNorm(bounds, ncolors=cmap_custom.N, clip=True)

# Configuración de los subplots
fig, axes = plt.subplots(nrows=3, ncols=8, figsize=(10, 5), subplot_kw={'projection': ccrs.PlateCarree()})
fig.subplots_adjust(wspace=0.3, hspace=0.3)  # Ajustar el espaciado

# Nombres de los meses
meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Plotear los datos de CAMS y MERRA-2
for i, mes in enumerate(meses):
    row, col = divmod(i, 4)
    ax_cams = axes[row, col * 2]
    ax_merra = axes[row, col * 2 + 1]
    
    # Plot CAMS
    pcm_cams = ax_cams.pcolormesh(lons, lats, aod_cams[i, :, :], transform=ccrs.PlateCarree(), cmap=cmap_custom, norm=norm)
    ax_cams.coastlines()
    ax_cams.set_extent([-81, -34, -56, 10], crs=ccrs.PlateCarree())
    ax_cams.add_feature(cfeature.BORDERS)
    ax_cams.add_feature(cfeature.COASTLINE)
    ax_cams.set_title(f'CAMS - {mes}', fontsize=6)
    
    # Plot MERRA-2
    pcm_merra = ax_merra.pcolormesh(lons, lats, aod_merra[i, :, :], transform=ccrs.PlateCarree(), cmap=cmap_custom, norm=norm)
    ax_merra.coastlines()
    ax_merra.set_extent([-81, -34, -56, 10], crs=ccrs.PlateCarree())
    ax_merra.add_feature(cfeature.BORDERS)
    ax_merra.add_feature(cfeature.COASTLINE)
    ax_merra.set_title(f'MERRA-2 - {mes}', fontsize=6)

# Añadir barras de colores
cbar_ax = fig.add_axes([0.92, 0.1, 0.02, 0.79])  # Ajusta la posición y altura de la colorbar
cbar = fig.colorbar(pcm_cams, cax=cbar_ax, boundaries=bounds, ticks=bounds)
cbar.set_label('Black Carbon 550nm', fontsize=8, labelpad=15)
cbar.ax.tick_params(labelsize=8) 

# Guardar y mostrar la figura
plt.savefig('C:/Users/ferfo/OneDrive/Escritorio/aod-bc-cams-merra.png', dpi=300, bbox_inches='tight')
plt.show()
