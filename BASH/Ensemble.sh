#!/bin/bash

# Directorio donde se encuentran los archivos de los modelos
MODELS_DIR="/mnt/c/Users/ferfo/OneDrive/Desktop/terminado"
# Directorio temporal para almacenar los archivos anuales y los promedios mensuales
TEMP_DIR="$MODELS_DIR/temp"
# Directorio donde se guardarán los resultados finales
RESULTS_DIR="$MODELS_DIR/c"

# Crear directorios temporales y de resultados
mkdir -p $TEMP_DIR
mkdir -p $RESULTS_DIR

# Procesar cada archivo de modelo en el directorio
for model_file in $MODELS_DIR/*.nc; do
    model_name=$(basename $model_file .nc)
    model_temp_dir="$TEMP_DIR/$model_name"
    model_result_dir="$RESULTS_DIR/$model_name"

    # Crear directorio temporal para el modelo actual
    mkdir -p $model_temp_dir

    # Crear directorio de resultados específico para el modelo
    mkdir -p $model_result_dir

    echo "Procesando modelo: $model_name"

    # Separar los datos por año
    for year in $(seq 2003 2014); do
        echo "Seleccionando datos para el año $year del archivo $model_file"
        cdo selyear,$year $model_file $model_temp_dir/year_$year.nc
        if [ $? -ne 0 ]; then
            echo "Error al seleccionar datos para el año $year del archivo $model_file"
            exit 1
        fi
    done

    # Verificar que los archivos anuales se han creado correctamente
    for year in $(seq 2003 2014); do
        if [ ! -f $model_temp_dir/year_$year.nc ]; then
            echo "Archivo $model_temp_dir/year_$year.nc no encontrado"
            exit 1
        fi
    done

    # Calcular el promedio mensual para cada año
    for year in $(seq 2003 2014); do
        echo "Calculando el promedio mensual para el año $year"
        cdo monmean $model_temp_dir/year_$year.nc $model_temp_dir/monthly_mean_$year.nc
        if [ $? -ne 0 ]; then
            echo "Error al calcular el promedio mensual para el año $year"
            exit 1
        fi
    done

    # Borrar los archivos anuales temporales
    echo "Limpiando archivos temporales anuales para $model_name"
    rm $model_temp_dir/year_*.nc

    # Combinar todos los promedios mensuales en un solo archivo
    echo "Combinando los promedios mensuales para $model_name"
    cdo mergetime $model_temp_dir/monthly_mean_*.nc $model_result_dir/${model_name}_all_monthly_means.nc
    if [ $? -ne 0 ]; then
        echo "Error al combinar los promedios mensuales para $model_name. Verifica los permisos y la disponibilidad de espacio."
        exit 1
    fi

    # Borrar los archivos mensuales temporales
    echo "Limpiando archivos temporales mensuales para $model_name"
    rm $model_temp_dir/monthly_mean_*.nc

    # Borrar el directorio temporal específico del modelo
    rmdir $model_temp_dir
done

# Borrar el directorio temporal
rmdir $TEMP_DIR

echo "Procesamiento completado para todos los modelos. Los resultados se guardaron en la carpeta 'c'."

