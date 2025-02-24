# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:45:49 2024

@author: ferfo
"""

import os
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

class TaylorDiagram(object):
    def __init__(self, refstd, fig=None, rect=111, label='_', srange=(0, 2), extend=False):  # Ajuste del rango a 2
        from matplotlib.projections import PolarAxes
        import mpl_toolkits.axisartist.floating_axes as FA
        import mpl_toolkits.axisartist.grid_finder as GF

        self.refstd = refstd
        tr = PolarAxes.PolarTransform()
        rlocs = np.array([0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 1])
        if extend:
            self.tmax = np.pi
            rlocs = np.concatenate((-rlocs[:0:-1], rlocs))
        else:
            self.tmax = np.pi / 2
        tlocs = np.arccos(rlocs)
        gl1 = GF.FixedLocator(tlocs)
        tf1 = GF.DictFormatter(dict(zip(tlocs, map(str, rlocs))))
        self.smin = srange[0] * self.refstd
        self.smax = srange[1] * self.refstd

        ghelper = FA.GridHelperCurveLinear(tr, extremes=(0, self.tmax, self.smin, self.smax), grid_locator1=gl1, tick_formatter1=tf1)

        if fig is None:
            fig = plt.figure()

        ax = FA.FloatingSubplot(fig, rect, grid_helper=ghelper)
        fig.add_subplot(ax)

        ax.axis["top"].set_axis_direction("bottom")
        ax.axis["top"].toggle(ticklabels=True, label=True)
        ax.axis["top"].major_ticklabels.set_axis_direction("top")
        ax.axis["top"].label.set_axis_direction("top")
        ax.axis["top"].label.set_text("Correlation")

        ax.axis["left"].set_axis_direction("bottom")
        ax.axis["left"].label.set_text("Standard deviation")

        ax.axis["right"].set_axis_direction("top")
        ax.axis["right"].toggle(ticklabels=True)
        ax.axis["right"].major_ticklabels.set_axis_direction("bottom" if extend else "left")

        if self.smin:
            ax.axis["bottom"].toggle(ticklabels=False, label=False)
        else:
            ax.axis["bottom"].set_visible(False)

        self._ax = ax
        self.ax = ax.get_aux_axes(tr)

        # Adjust the position of the standard deviation tick labels
        ax.axis["left"].major_ticklabels.set_pad(10)  # Increase padding between tick labels and axis
        ax.axis["right"].major_ticklabels.set_pad(10)
        l, = self.ax.plot([0], self.refstd, 'k*', ls='', ms=10, label=label)
        t = np.linspace(0, self.tmax)
        r = np.zeros_like(t) + self.refstd
        self.ax.plot(t, r, 'k--', label='_')
        self.samplePoints = [l]

    def add_sample(self, stddev, corrcoef, *args, **kwargs):
        l, = self.ax.plot(np.arccos(corrcoef), stddev, *args, **kwargs)
        self.samplePoints.append(l)
        return l

    def add_grid(self, *args, **kwargs):
        self._ax.grid(*args, **kwargs)

    def add_contours(self, levels=5, **kwargs):
        rs, ts = np.meshgrid(np.linspace(self.smin, self.smax), np.linspace(0, self.tmax))
        rms = np.sqrt(self.refstd ** 2 + rs ** 2 - 2 * self.refstd * rs * np.cos(ts))
        contours = self.ax.contour(ts, rs, rms, levels, **kwargs)
        return contours

# Función para leer la variable de un archivo NetCDF
def read_nc_variable(file_path, var_name):
    dataset = xr.open_dataset(file_path)
    variable = dataset[var_name].values
    return variable

# Ruta a la carpeta con los modelos
models_folder = 'C:/Users/ferfo/OneDrive/Desktop/bc'

# Archivo de referencia
reference_file = 'C:/Users/ferfo/OneDrive/Desktop/bc/camsbc.nc'
reference_variable = 'bcaod550'

# Leer la variable de referencia
reference_data = read_nc_variable(reference_file, reference_variable)

# Inicializar listas para las estadísticas de los modelos
model_names = []
stddev = []
correlation = []

# Recorrer los archivos en la carpeta de modelos
for file_name in os.listdir(models_folder):
    if file_name.endswith('.nc') and file_name != 'camsbc.nc':
        model_file = os.path.join(models_folder, file_name)
        model_data = read_nc_variable(model_file, 'od550bc')

        # Calcular la desviación estándar y la correlación con el archivo de referencia
        model_name, _ = os.path.splitext(file_name)  # Eliminar la extensión .nc
        model_names.append(model_name)
        stddev.append(np.std(model_data))
        correlation.append(np.corrcoef(reference_data.flatten(), model_data.flatten())[0, 1])

# Convertir las listas a numpy arrays para el diagrama de Taylor
stddev = np.array(stddev)
correlation = np.array(correlation)
reference_stddev = np.std(reference_data)

# Crear el diagrama de Taylor
fig = plt.figure(figsize=(10, 8))
dia = TaylorDiagram(reference_stddev, fig=fig, label='CAMS', extend=True)

# Tamaño de los puntos
marker_size = 8

# Añadir los modelos al diagrama de Taylor con bordes negros y colores específicos según la correlación
for i, (std, corr) in enumerate(zip(stddev, correlation)):
    color = '#B22222' if corr < 0.7 else '#6495ED'
    dia.add_sample(std, corr, marker='o', ms=marker_size, ls='', mfc=color, mec='k', mew=1, label=model_names[i])

# Añadir una cuadrícula
dia.add_grid()

# Añadir contornos de RMS
contours = dia.add_contours(levels=5, colors='0.5')
plt.clabel(contours, inline=1, fontsize=10, fmt='%.2f')

# Añadir leyenda debajo del plot con 6 modelos por columna
plt.legend(dia.samplePoints, [p.get_label() for p in dia.samplePoints], numpoints=1, prop=dict(size='small'), loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=6)

# Título
plt.title('Black carbon at 550 nm', pad=40)

# Guardar la figura
plt.savefig('AODbc.png', dpi=300, bbox_inches='tight')
plt.show()

