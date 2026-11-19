# Fase 3: análisis de asimetrías

## ¿Qué mide la asimetría?

Una distribución es simétrica cuando la media y la mediana coinciden. Si la
media se separa de la mediana, es porque una cola de valores extremos la está
"tirando" hacia ese lado: si la media es mayor, la cola derecha es más larga
(asimetría positiva); si es menor, lo es la izquierda (asimetría negativa).

El coeficiente de asimetría (momento de tercer orden, corregido por tamaño
muestral) cuantifica esa falta de simetría: valores cercanos a 0 indican
simetría; valores positivos, cola derecha; negativos, cola izquierda. En
presencia de asimetría o atípicos, la **mediana y los percentiles** describen
mejor el centro que la media y el desvío estándar.

## Datos crudos (los que usa hoy `fase_2_consola.py`)

| Variable | n | Media | Mediana | Media − Mediana | Diferencia relativa | Asimetría |
|---|---:|---:|---:|---:|---:|---:|
| `salario` | 245 | 440.514,47 | 436.124,02 | +4.390,45 | +1,01% | −0,182 |
| `ganancias_sector` | 258 | 414.575,21 | 353.740,98 | +60.834,23 | +17,20% | +15,826 |

### Salario

La distribución es **casi simétrica**: la media supera a la mediana en apenas
el 1,01%. El coeficiente negativo (−0,182) no indica una tendencia real de la
población, sino el efecto del registro inválido de **−150.000**, que estira la
cola izquierda. Al excluir ese valor, la media sube a 442.934,61, la mediana a
437.615,01 y el coeficiente pasa a **+0,222**: una asimetría derecha leve y
perfectamente normal en variables de ingresos.

### Ganancias por sector

Aquí la asimetría es **extrema** (15,826): la media está un 17,2% por encima de
la mediana. Pero este resultado es **completamente artificial**. Al retirar el
único registro de **15.000.000** —un error de carga— la media cae a 357.822,59,
la diferencia con la mediana se reduce a 4.246,02 (1,2%) y el coeficiente baja
a **+0,178**. Es decir, `ganancias_sector` es casi simétrica y todo el
"sesgo" era ese único outlier.

## Datos después de la limpieza (`proyecto_3_todos_al_agua_limpio.csv`)

| Variable | n | Media | Mediana | Desvío | Asimetría |
|---|---:|---:|---:|---:|---:|
| `salario` | 250 | 441.748,05 | 439.540,55 | 116.192,20 | +0,181 |
| `ganancias_sector` | 250 | 356.280,97 | 353.658,78 | 88.393,34 | +0,102 |

Tras imputar los valores nulos e inválidos con la mediana de su grupo, ambas
variables quedan con asimetría leve y positiva, coherente con ingresos: la
media apenas supera a la mediana (0,50% en salario y 0,74% en ganancias) y los
desvíos son del orden del 25% de la media, sin distorsiones.

## Conclusión

- Los estadísticos crudos de `ganancias_sector` **no son interpretables**:
  debe informarse la mediana (353.740,98) y el rango intercuartílico
  (Q1 = 293.536,24; Q3 = 418.708,71), nunca la media de 414.575,21.
- Para `salario` basta con documentar que la asimetría es leve y que el valor
  negativo fue un error de carga ya corregido en la Fase 2.
- Este análisis justifica por qué la Fase 2 imputó con la **mediana** y no con
  la media ni con cero: la mediana es robusta frente a los dos outliers y no
  introduce ingresos falsos.
