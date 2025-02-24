# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:11:10 2024

@author: ferfo
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos de cada hoja
file_path = 'C:/Users/ferfo/OneDrive/Escritorio/total.xlsx'  # Reemplaza con la ruta correcta a tu archivo
total_data = pd.read_excel(file_path, sheet_name='Total')
bc_data = pd.read_excel(file_path, sheet_name='bc')
org_data = pd.read_excel(file_path, sheet_name='org')

# Establecer un diccionario de estilos para las líneas punteadas y colores
dashed_lines = ['MERRA-2', 'CAMS', 'Ensemble', 'Ensemble Org', 'Ensemble Bc']  # Usamos "Ensemble"
color_mapping = {
    'Ensemble': 'black',
    'Ensemble Org': 'black',
    'Ensemble Bc': 'black',
    'MERRA-2': '#008B8B',  # Color especificado para MERRA-2
    'CAMS': '#8B008B'      # Color especificado para CAMS
}

# Lista de los 12 meses
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Función para renombrar las columnas de Ensamble a Ensemble
def rename_columns(df):
    df = df.rename(columns={
        'Ensamble': 'Ensemble',
        'Ensamble Org': 'Ensemble Org',
        'Ensamble Bc': 'Ensemble Bc'
    })
    return df

# Renombrar columnas en cada dataframe
total_data = rename_columns(total_data)
bc_data = rename_columns(bc_data)
org_data = rename_columns(org_data)

# --------- Primera figura: Datos de 'Total' ---------
fig1, ax1 = plt.subplots(figsize=(10, 6))

for column in total_data.columns[1:]:  # Saltar la primera columna si es el índice
    linestyle = '--' if column in ['Ensemble', 'CAMS'] else '-'  # Línea punteada para Ensemble y CAMS
    color = color_mapping.get(column, None)  
    ax1.plot(total_data.index, total_data[column], label=column, linestyle=linestyle, color=color)

ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Total AOD at 550 nm', fontsize=14)
ax1.set_ylim(0, 0.4)
ax1.set_xticks(range(12))  
ax1.set_xticklabels(meses, fontsize=12)  

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.tight_layout()
fig1.savefig('C:/Users/ferfo/OneDrive/Escritorio/total_data_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# --------- Segunda figura: Datos de 'bc' ---------
fig2, ax2 = plt.subplots(figsize=(10, 6))

for column in bc_data.columns[1:]:
    linestyle = '--' if column in ['Ensemble Bc', 'CAMS'] else '-'  
    color = color_mapping.get(column, None)  
    ax2.plot(bc_data.index, bc_data[column], label=column, linestyle=linestyle, color=color)

ax2.set_xlabel('Month', fontsize=14)
ax2.set_ylabel('Black carbon at 550 nm', fontsize=14)
ax2.set_ylim(0, 0.030)
ax2.set_xticks(range(12))
ax2.set_xticklabels(meses, fontsize=12)

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.tight_layout()
fig2.savefig('C:/Users/ferfo/OneDrive/Escritorio/bc_data_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# --------- Tercera figura: Datos de 'org' ---------
fig3, ax3 = plt.subplots(figsize=(10, 6))

for column in org_data.columns[1:]:
    linestyle = '--' if column in ['Ensemble Org', 'CAMS'] else '-'  
    color = color_mapping.get(column, None)  
    ax3.plot(org_data.index, org_data[column], label=column, linestyle=linestyle, color=color)

ax3.set_xlabel('Month', fontsize=14)
ax3.set_ylabel('Organic aerosol at 550 nm', fontsize=14)
ax3.set_ylim(0, 0.2)
ax3.set_xticks(range(12))
ax3.set_xticklabels(meses, fontsize=12)

ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4)
plt.tight_layout()
fig3.savefig('C:/Users/ferfo/OneDrive/Escritorio/org_data_plot.png', dpi=300, bbox_inches='tight')
plt.show()


