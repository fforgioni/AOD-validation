# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:11:10 2024

@author: ferfo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos de cada hoja
file_path = 'C:/Users/ferfo/OneDrive/Desktop/total.xlsx'  # Reemplaza con la ruta correcta a tu archivo
total_data = pd.read_excel(file_path, sheet_name='Total')
bc_data = pd.read_excel(file_path, sheet_name='bc')
org_data = pd.read_excel(file_path, sheet_name='org')

# Establecer un diccionario de estilos para las líneas punteadas y colores
dashed_lines = ['MERRA-2', 'CAMS', 'Ensamble', 'Ensamble Org', 'Ensamble Bc']  # Agregamos Ensamble Org, Ensamble Bc, y CAMS
color_mapping = {
    'Ensamble': 'black',
    'Ensamble Org': 'black',
    'Ensamble Bc': 'black',
    'MERRA-2': '#008B8B',  # Color especificado para MERRA-2
    'CAMS': '#8B008B'      # Color especificado para CAMS, con línea punteada
}

# Lista de los 12 meses
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# --------- Primera figura: Datos de 'Total' ---------
fig1, ax1 = plt.subplots(figsize=(10, 6))

for column in total_data.columns[1:]:  # Saltar la primera columna si es el índice
    linestyle = '--' if column in ['Ensamble', 'CAMS'] else '-'  # Línea punteada para Ensamble y CAMS
    color = color_mapping.get(column, None)  # Usar color asignado o dejar que Matplotlib asigne uno automáticamente
    ax1.plot(total_data.index, total_data[column], label=column, linestyle=linestyle, color=color)
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Total AOD at 550 nm', fontsize=14)

# Ajustar los límites del eje Y para el gráfico de 'Total'
ax1.set_ylim(0, 0.4)

# Colocar los 12 meses en el eje X
ax1.set_xticks(range(12))  # Establecer 12 ticks para los meses
ax1.set_xticklabels(meses, fontsize=12)  # Etiquetas con los nombres de los meses

# Colocar la leyenda debajo del gráfico con 6 datos por columna
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

# Ajustar el layout y guardar la figura con la leyenda incluida
plt.tight_layout()
fig1.savefig('C:/Users/ferfo/OneDrive/Desktop/total_data_plot.png', dpi=300, bbox_inches='tight')

# Mostrar la primera figura
plt.show()

# --------- Segunda figura: Datos de 'bc' ---------
fig2, ax2 = plt.subplots(figsize=(10, 6))

for column in bc_data.columns[1:]:
    linestyle = '--' if column in ['Ensamble Bc', 'CAMS'] else '-'  # Línea punteada para Ensamble Bc y CAMS
    color = color_mapping.get(column, None)  # Usar color asignado o dejar que Matplotlib asigne uno automáticamente
    ax2.plot(bc_data.index, bc_data[column], label=column, linestyle=linestyle, color=color)
ax2.set_xlabel('Month', fontsize=14)
ax2.set_ylabel('Black carbon at 550 nm', fontsize=14)

# Ajustar los límites del eje Y para el gráfico de 'BC'
ax2.set_ylim(0, 0.030)

# Colocar los 12 meses en el eje X
ax2.set_xticks(range(12))
ax2.set_xticklabels(meses, fontsize=12)

# Colocar la leyenda debajo del gráfico con 6 datos por columna
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

# Ajustar el layout y guardar la figura con la leyenda incluida
plt.tight_layout()
fig2.savefig('C:/Users/ferfo/OneDrive/Desktop/bc_data_plot.png', dpi=300, bbox_inches='tight')

# Mostrar la segunda figura
plt.show()

# --------- Tercera figura: Datos de 'org' ---------
fig3, ax3 = plt.subplots(figsize=(10, 6))

for column in org_data.columns[1:]:
    linestyle = '--' if column in ['Ensamble Org', 'CAMS'] else '-'  # Línea punteada para Ensamble Org y CAMS
    color = color_mapping.get(column, None)  # Usar color asignado o dejar que Matplotlib asigne uno automáticamente
    ax3.plot(org_data.index, org_data[column], label=column, linestyle=linestyle, color=color)
ax3.set_xlabel('Month', fontsize=14)
ax3.set_ylabel('Organic aerosol at 550 nm', fontsize=14)

# Ajustar los límites del eje Y para el gráfico de 'Org'
ax3.set_ylim(0, 0.2)

# Colocar los 12 meses en el eje X
ax3.set_xticks(range(12))
ax3.set_xticklabels(meses, fontsize=12)

# Colocar la leyenda debajo del gráfico con 6 datos por columna
ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)

# Ajustar el layout y guardar la figura con la leyenda incluida
plt.tight_layout()
fig3.savefig('C:/Users/ferfo/OneDrive/Desktop/org_data_plot.png', dpi=300, bbox_inches='tight')

# Mostrar la tercera figura
plt.show()


