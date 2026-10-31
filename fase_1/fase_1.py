import pandas as pd
import numpy as np
# Análisis estructural: dimensiones, tipos de datos y detección inicial de anomalías
# Carga Archivo de datos
df = pd.read_csv("proyecto_3_todos_al_agua_crudo.csv")

# Analisis estructural general del data frame
df.info()

# Detección Inicial de Anomalías
print("DETECCION DE ANOMALIAS")
print("1- FILAS SIN NUMEROS ASIGNADOS (NAN)")
# df.isna().sum() detectamos de acuerdo a cada columna la cantidad de filas sin numeros asignados (NAN) y lo sumamos a su columna correspondiente
arr_nan = [df.isna().sum()]
print(arr_nan)

print("2- FILAS DUPLICADAS")
# subset=None considerará que una fila es duplicada solo si todas sus columnas son idénticas.
# keep='first' conserva la primera aparicion y elimina el duplicado siguiente si aparece
# inplace=False devuelve una copia del original sin modificar la original
# ignore_index=True para reestablecer los indices (IDs) de las columnas
arr_dup = [df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=True)]
print(arr_dup)

