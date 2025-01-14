# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:33:43 2024

@author: ferfo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel
file_path = 'C:/Users/ferfo/OneDrive/Desktop/metricas org.xlsx'  # Reemplaza con la ruta correcta a tu archivo
data = pd.read_excel(file_path)

# Crear una figura con dos subplots: uno para RMSE y otro para BIAS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

# Crear una paleta única con base en los modelos
unique_models = data['Modelo'].unique()
palette_rmse = sns.color_palette('husl', len(unique_models))  # Paleta de colores variada para los modelos

# Graficar los valores de RMSE en el primer subplot con seaborn
sns.barplot(x='Modelo', y='RMSE', data=data, ax=ax1, palette=palette_rmse)
ax1.set_xlabel('Model', fontsize=20)
ax1.set_ylabel('RMSE', fontsize=20)
ax1.tick_params(axis='x', rotation=90, labelsize=20)  # Ajustar el tamaño de los ticks del eje x
ax1.tick_params(axis='y', labelsize=20)  # Ajustar el tamaño de los ticks del eje y

# Ajustar los límites del eje Y para el gráfico de RMSE (de 0 a 0.16)
ax1.set_ylim(0, 0.2)

# Añadir el texto "(a)" en la esquina superior izquierda del primer gráfico
ax1.text(0.05, 0.9, '(a)', transform=ax1.transAxes, fontsize=24)

# Graficar los valores de BIAS en el segundo subplot con seaborn
sns.barplot(x='Modelo', y='BIAS', data=data, ax=ax2, palette=palette_rmse)  # Usamos la misma paleta para consistencia
ax2.set_xlabel('Model', fontsize=20)
ax2.set_ylabel('BIAS', fontsize=20)
ax2.tick_params(axis='x', rotation=90, labelsize=20)  # Ajustar el tamaño de los ticks del eje x
ax2.tick_params(axis='y', labelsize=20)  # Ajustar el tamaño de los ticks del eje y

# Ajustar los límites del eje Y para el gráfico de BIAS (de -0.10 a 0.10)
ax2.set_ylim(-0.10, 0.2)

# Añadir el texto "(b)" en la esquina superior izquierda del segundo gráfico
ax2.text(0.05, 0.9, '(b)', transform=ax2.transAxes, fontsize=24)

# Ajustar el layout para evitar solapamientos
plt.tight_layout()

# Guardar la figura antes de mostrarla
fig.savefig('C:/Users/ferfo/OneDrive/Desktop/grafico_org.png', dpi=300)  # Guardar como PNG a 300 DPI

# Mostrar los gráficos
plt.show()
