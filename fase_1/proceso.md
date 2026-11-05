
**Fase 1: Diagnóstico e Inspección Inicial (Módulo 1)**
•Carga del archivo crudo utilizando pandas.
•Análisis estructural: dimensiones, tipos de datos y detección inicial de
anomalías.
•Auditoría de calidad: conteo y localización de valores nulos (NaN) y filas
duplicadas exactas.

Ejecutamos en consola "*python proyecto_3_todos_al_agua_crudo.py*" para extraer los datos en crudo a formato .csv

**Resultado del diagnostico:**
•258 filas y 10 columnas, con tipos int64, float64, str y bool.
•33 nan en total: sectores 11, salario 13 y tipo_discapacidad 9. Es un 4,2% de las celdas, por eso se imputa y no se elimina (regla del 0 al 5%).
•8 filas duplicadas exactas (los ids 3081 a 3088 repetidos), se quitan con drop_duplicates().

**Limpieza aplicada:**
•La limpieza se hace sobre una copia del df original, el archivo crudo queda sin tocar.
•Primero se eliminan los duplicados y despues se rellenan los nan, porque si rellenamos antes se pueden borrar filas reales.
•Los nan de salario van con 0 por ser una columna numerica.
•Los nan de sectores y tipo_discapacidad van con "Sin dato" porque son columnas de texto.
