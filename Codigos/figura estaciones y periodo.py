# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:33:08 2024

@author: ferfo
"""

import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Cargar los datos desde el archivo Excel
file_path = 'C:/Users/ferfo/OneDrive/Desktop/estaciones.xlsx'  # Ajusta la ruta al archivo
estaciones_data = pd.read_excel(file_path, sheet_name='Merra')

# Extraer las estaciones
stations = estaciones_data.set_index('estacion').to_dict('index')

# Crear la figura y el mapa de fondo
fig = plt.figure(figsize=(18, 14))  # Hacer la figura más grande
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-85, -30, -60, 15], crs=ccrs.PlateCarree())  # Enfocar en Sudamérica

# Agregar fondo de relieve
ax.stock_img()
ax.add_feature(cfeature.BORDERS, linestyle=':')  # Límites de países
ax.add_feature(cfeature.COASTLINE)  # Costa

# Crear leyenda personalizada
legend_labels = []

# Plotear las estaciones con números
for i, (name, info) in enumerate(stations.items(), start=1):
    ax.plot(info['longitud'], info['latitud'], marker='o', color='black', markersize=25, transform=ccrs.PlateCarree())
    
    # Añadir el número en negro sobre el marcador
    ax.text(info['longitud'], info['latitud'], str(i), color='white', fontsize=12,
            ha='center', va='center', weight='bold', transform=ccrs.PlateCarree())
    
    # Agregar a la leyenda
    legend_labels.append(f"{i}. {name}")

# Mostrar la leyenda al lado del mapa
plt.figtext(
    0.75,  # Ajusta este valor para mover horizontalmente (más hacia la derecha)
    0.5,  # Ajusta este valor para mover verticalmente (más hacia arriba o abajo)
    "\n".join(legend_labels),
    fontsize=20,
    ha='left',
    va='center',
    bbox=dict(facecolor='whitesmoke', edgecolor='black')
)

# # Agregar un título a la figura
# plt.suptitle(
#     "AERONET Stations over South America",
#     fontsize=24,  # Tamaño de fuente
#     weight='bold',  # Texto en negrita
#     y=0.91  # Posición vertical (ajusta si es necesario)
# )

# Guardar la figura en un archivo antes de mostrarla
plt.savefig('C:/Users/ferfo/OneDrive/Desktop/sudamerica_estaciones_numeradas_grande.png', dpi=300, bbox_inches='tight', transparent=False)

plt.show()

