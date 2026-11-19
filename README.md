# TP Final Integrador – Proyecto III: Todos al Agua

Análisis de datos sobre un dataset sintético de 258 participantes de
actividades acuáticas, con ruido, nulos, duplicados y anomalías.

## Estructura

| Archivo / carpeta                                              | Contenido                                                                                                       |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `proyecto_3_todos_al_agua_crudo.py`                          | Generador único del CSV crudo                                                                                  |
| `proyecto_3_todos_al_agua_crudo.csv`                         | Dataset crudo único (258 filas)                                                                                |
| `fase_1/`                                                    | Diagnóstico y limpieza (Lisandro): `fase_1.py`, `proceso.md`, su CSV exportado y el CSV limpio del notebook |
| `fase_2/`                                                    | Estadística, IQR y gráficos (Fragiee) + sus 3 PNG originales                                                  |
| `informe/`                                                   | Asimetrías, conclusiones y 3 gráficos sobre datos limpios                                                     |
| `TP_Final_Todos_al_Agua.ipynb`                               | Notebook conjunto con las cuatro fases                                                                          |
| `Trabajo Práctico Final Integrador - Analisis de Datos.pdf` | Enunciado                                                                                                       |

## Ejecución

```bash
pip install -r requirements.txt
python proyecto_3_todos_al_agua_crudo.py     # si hay que regenerar el crudo
cd fase_1
python fase_1.py                              # lee ../proyecto_3_todos_al_agua_crudo.csv
cd ..
cd fase_2
python fase_2_consola.py
python fase_2_grafica.py
cd ..
jupyter notebook TP_Final_Todos_al_Agua.ipynb
```

El notebook se ejecuta desde la raíz y guarda sus imágenes en `informe/`.
Los scripts de `fase_2` se ejecutan desde dentro de `fase_2` y sobrescriben
sus 3 PNG con los datos del CSV que leen. El generador escribe siempre el CSV
crudo al lado de sí mismo.

## Resultados clave

- 258 filas crudas → 250 limpias (8 duplicados eliminados), 0 nulos.
- 33 celdas nulas imputadas con "Sin dato" o mediana por grupo.
- 2 errores de carga marcados e imputados: salario −150.000 y ganancias 15.000.000.
- Mediana salarial 439.541; mediana de ganancias 353.659.
- El outlier de 15.000.000 era el único responsable de la asimetría extrema
  de `ganancias_sector` (15,83 → 0,18).

## Coordinación

Los scripts de `fase_2/` ya no arman el `DataFrame` a mano: leen
`../fase_1/proyecto_3_todos_al_agua_limpio_fase1.csv` (el CSV exportado por
`fase_1.py`). El resto del código de Fran —cálculos, IQR y gráficos— quedó
intacto.

Ese CSV ya no tiene duplicados ni el 15.000.000 (se corrigió con la regla IQR),
pero todavía conserva los salarios en 0. Para usar la versión corregida del
todo, alcanza con cambiar la ruta por
`../fase_1/proyecto_3_todos_al_agua_limpio.csv`.
