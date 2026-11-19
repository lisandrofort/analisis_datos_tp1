import pandas as pd
import numpy as np
# Análisis estructural: dimensiones, tipos de datos y detección inicial de anomalías
# Carga Archivo de datos: ".." sube una carpeta, donde esta el CSV crudo
df = pd.read_csv("../proyecto_3_todos_al_agua_crudo.csv")

# Analisis estructural general del data frame
df.info()
print("Dimensiones:", df.shape)

# Detección Inicial de Anomalías
print("DETECCION DE ANOMALIAS")
print("1- FILAS SIN NUMEROS ASIGNADOS (NAN)")
# df.isna().sum() detectamos de acuerdo a cada columna la cantidad de filas sin numeros asignados (NAN) y lo sumamos a su columna correspondiente
print(df.isna().sum())
# localizamos las filas que tienen al menos un nan
print(df[df.isna().any(axis=1)])

print("2- FILAS DUPLICADAS")
# duplicated() marca True en la fila repetida, keep='first' conserva la primera aparicion
print("Cantidad de duplicados:", df.duplicated().sum())
print(df[df.duplicated(keep='first')])

# LIMPIEZA
# hacemos una copia del df original para no modificarlo
print("LIMPIEZA DE DATOS")
arr_final = df.copy()

# 1) quitamos los duplicados
# subset=None considerará que una fila es duplicada solo si todas sus columnas son idénticas.
# keep='first' conserva la primera aparicion y elimina el duplicado siguiente si aparece
# ignore_index=True para reestablecer los indices (IDs) de las columnas
arr_final = arr_final.drop_duplicates(subset=None, keep='first', ignore_index=True)

# 2) rellenamos los nan (siempre despues de quitar duplicados)
# salario es una columna numerica -> 0
arr_final["salario"] = arr_final["salario"].fillna(0)
# sectores y tipo_discapacidad son texto -> no pueden ir con 0
arr_final["sectores"] = arr_final["sectores"].fillna("Sin dato")
arr_final["tipo_discapacidad"] = arr_final["tipo_discapacidad"].fillna("Sin dato")

print("NAN restantes:")
print(arr_final.isna().sum())
print("Dimensiones del arreglo limpio:", arr_final.shape)
# el df original queda intacto
print("Dimensiones del original:", df.shape)

# VARIABLE DERIVADA: marcamos si el participante es adulto o no.
# Es solo una comparacion: si la edad es 18 o mas da True, si no da False.
arr_final["es_adulto"] = arr_final["edad"] >= 18

# AGRUPAMIENTO: contamos participantes y sacamos el salario mediano
# de cada actividad. agg() permite pedir varias cuentas a la vez.
resumen = arr_final.groupby("actividades")["salario"].agg(["count", "median"])
print("Resumen por actividad:")
print(resumen)