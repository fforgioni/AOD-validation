# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:09:55 2024

@author: ferfo
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Cargar el archivo de Excel
file_path = 'C:/Users/ferfo/OneDrive/Desktop/climatologia_mensual.xlsx'
climatologia_df = pd.read_excel(file_path)

# Configuración del estilo de Seaborn
sns.set(style="whitegrid")

# Definir los colores para las barras
colors = ['#6495ED' if mes not in ['August', 'September', 'October'] else '#B22222' for mes in climatologia_df['mes']]

# Crear el plot
plt.figure(figsize=(10, 6))
plot = sns.barplot(x='mes', y='incendios', data=climatologia_df, palette=colors)

# Añadir etiquetas y título
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of fire pixlels', fontsize=14)
#plt.title('Monthly fire pixles over South America. 2003-2023', fontsize=16)

# Ajustar el tamaño de las etiquetas de los ejes y rotarlas 45°
plot.set_xticklabels(plot.get_xticklabels(), fontsize=12, rotation=45)

# Establecer los límites del eje y
plot.set_ylim(0, 1400000)

# Formatear las etiquetas del eje y para que no tengan decimales
formatter = FuncFormatter(lambda x, _: f'{int(x):,}')
plot.yaxis.set_major_formatter(formatter)

# Guardar el plot
plt.tight_layout()
plt.savefig('C:/Users/ferfo/OneDrive/Desktop/climatologia_mensual_colores.png', dpi=300, bbox_inches='tight')

# Mostrar el plot
plt.show()


