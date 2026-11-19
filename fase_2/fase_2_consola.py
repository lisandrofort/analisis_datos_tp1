import pandas as pd
import numpy as np

df3 = pd.read_csv('../fase_1/proyecto_3_todos_al_agua_limpio_fase1.csv')


fin_cols = ['ganancias_sector', 'salario']

for col in fin_cols:
    s = df3[col].dropna()
    print(f"--- Variable: {col} ---")
    print("Media:", s.mean())
    print("Mediana:", s.median())
    print("Desviación Estándar:", s.std())
    print("Percentiles (10, 25, 50, 75, 90):", s.quantile([0.1, 0.25, 0.5, 0.75, 0.9]).to_dict())
    
    Q1 = s.quantile(0.25)
    Q3 = s.quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    outliers = s[(s < lower_limit) | (s > upper_limit)]
    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
    print(f"Límites: [{lower_limit}, {upper_limit}]")
    print(f"Cantidad de atípicos: {len(outliers)}")
    print("Valores atípicos:", outliers.tolist())
    print()

