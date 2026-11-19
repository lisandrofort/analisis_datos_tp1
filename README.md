# TP Final Integrador – Proyecto III: Todos al Agua

Análisis de datos sobre un dataset sintético de 258 participantes de
actividades acuáticas, con ruido, nulos, duplicados y anomalías.

## Estructura

| Archivo / carpeta                                              | Contenido                                                                                                       |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `proyecto_3_todos_al_agua_crudo.py`                          | Generador único del CSV crudo                                                                                  |
| `proyecto_3_todos_al_agua_crudo.csv`                         | Dataset crudo único (258 filas)                                                                                |
| `fase_1/`                                                    | Diagnóstico y limpieza básica (Lisandro): `fase_1.py` y `proceso.md`; el CSV limpio lo genera el notebook |
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
jupyter notebook TP_Final_Todos_al_Agua.ipynb
```

El notebook se puede ejecutar completo desde la raíz. Guarda sus imágenes en
`informe/` con sufijo `_limpio`; las de `fase_2/` son las originales de
tu compañero y no se sobrescriben. El generador escribe siempre el CSV crudo
al lado de sí mismo, así que no se crean copias en otras carpetas.

## Resultados clave

- 258 filas crudas → 250 limpias (8 duplicados eliminados), 0 nulos.
- 33 celdas nulas imputadas con "Sin dato" o mediana por grupo.
- 2 errores de carga marcados e imputados: salario −150.000 y ganancias 15.000.000.
- Mediana salarial 439.541; mediana de ganancias 353.741.
- El outlier de 15.000.000 era el único responsable de la asimetría extrema
  de `ganancias_sector` (15,83 → 0,18).

## Coordinación pendiente

Los scripts de `fase_2/` todavía reconstruyen el dataset crudo por su cuenta.
Deben pasar a leer `fase_1/proyecto_3_todos_al_agua_limpio.csv` para que sus
gráficos excluyan duplicados y valores inválidos. Ese cambio compete a la
persona responsable de esa carpeta.
