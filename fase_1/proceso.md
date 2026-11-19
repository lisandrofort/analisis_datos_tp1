# Fase 1: diagnóstico e inspección inicial

## Ejecución

El dataset crudo se genera desde la raíz del repositorio:

```bash
python proyecto_3_todos_al_agua_crudo.py
```

Luego se procesa con `python fase_1.py`, parándose dentro de la carpeta `fase_1`.

`fase_1.py` lee el crudo con `pd.read_csv("../proyecto_3_todos_al_agua_crudo.csv")`.
El `../` sube una carpeta: desde `fase_1` va a la raíz, donde está el CSV.
Por eso hay que ejecutarlo **desde dentro de la carpeta `fase_1`**:

```bash
cd fase_1
python fase_1.py
```

El CSV crudo es único y vive en la raíz.

## Análisis estructural

- Carga del archivo crudo con `pandas`.
- Dimensiones: **258 filas y 10 columnas**, con tipos `int64`, `float64`,
  `str` y `bool`.
- Auditoría de calidad: conteo y localización de nulos y duplicados exactos.

## Resultado del diagnóstico

- **33 celdas nulas**: `sectores` 11, `salario` 13 y `tipo_discapacidad` 9.
  - Son el **1,28% de las celdas** (33 de 2580) y el **12,79% de las filas**
    (33 filas, una celda nula por fila). El porcentaje correcto a informar es
    ese, no el 4,2%: el 4,26% corresponde solo a la columna `sectores` (11/258).
  - `salario` está en el 5,04% (13/258), apenas por encima de la regla del 5%.
    Se imputa y no se eliminan filas porque es una variable crítica y perder 13
    registros sesgaría más los resultados.
- **8 filas duplicadas exactas**: los IDs 3081 a 3088 aparecen dos veces (el
  generador los agrega al final de la lista). Se quitan con `drop_duplicates()`,
  quedando 250 participantes.
- **1 valor raro en `ganancias_sector`**: el participante 3089 tiene
  **15.000.000**, mientras la mediana es 353.741 y el resto está entre 135.000 y
  600.000. Es casi 40 veces el valor típico, probablemente un error de carga.

## Limpieza aplicada

Tal como está en `fase_1.py`:

- La limpieza se hace sobre una **copia** del DataFrame original; el crudo queda
  sin tocar.
- Primero se eliminan los duplicados y después se rellenan los nulos, porque si
  se rellena antes pueden borrarse filas reales.
- `salario` (numérica) → `0`.
- `sectores` y `tipo_discapacidad` (texto) → `"Sin dato"`.
- **Atípicos de ganancias**: con la regla del profe (`Q3 + 1.5 * IQR`) se
  detectan 2 valores arriba del límite y se reemplazan por la **mediana**, que
  es el valor del medio y no se deforma con el 15.000.000. Se conservan las filas.
- Resultado: **250 filas, 11 columnas, 0 nulos**.
- Al final se agregaron dos cosas simples para completar la Fase 2:
  - **Variable derivada**: `es_adulto`, que es `edad >= 18` (da `True` o `False`).
  - **Agrupamiento**: `groupby("actividades")["salario"].agg(["count", "median"])`,
    que muestra cuántos participantes hay y el salario mediano de cada actividad.
  - **Exportación**: `arr_final.to_csv("proyecto_3_todos_al_agua_limpio_fase1.csv", index=False)`.
    Se guarda en esta carpeta. Se llama distinto al CSV del notebook para no
    reemplazarlo (el del notebook tiene la imputación con mediana que usa el informe).

## Trabajo posterior (en el notebook)

El notebook `TP_Final_Todos_al_Agua.ipynb` toma el crudo y aplica un ETL más
completo: normaliza `tiene_cud` e `identidad_sexual`, imputa salario con la
mediana por actividad (en vez de 0), marca los dos errores de carga
(−150.000 y 15.000.000) y crea `rango_etario`. De ahí sale
`fase_1/proyecto_3_todos_al_agua_limpio.csv`, que es el dataset que usan el
análisis de asimetrías, las conclusiones y los gráficos limpios.

> Nota de coordinación: los scripts de `fase_2` leen
> `../fase_1/proyecto_3_todos_al_agua_limpio_fase1.csv`, que ya no tiene
> duplicados ni el 15.000.000. Todavía conserva los salarios en 0; por eso el
> informe y el notebook usan la versión corregida
> (`proyecto_3_todos_al_agua_limpio.csv`).
