import pandas as pd
import numpy as np
# Análisis estructural: dimensiones, tipos de datos y detección inicial de anomalías
# Carga Archivo de datos
df = pd.read_csv("proyecto_3_todos_al_agua_crudo.csv")

# Analisis estructural
df.info()

# Detección Inicial de Anomalías
print("DETECCION DE ANOMALIAS")
arr = [df.isna().sum()]
print(arr)

# 
