# Fase 4: conclusiones y propuestas estratégicas

Todo lo que sigue se calculó sobre `proyecto_3_todos_al_agua_limpio.csv`
(250 participantes, sin nulos, con categorías normalizadas y outliers
imputados).

## ¿Qué está pasando en el negocio?

La operación es estable en su centro: la mediana salarial es **439.541** y la
de ganancias por sector **353.659**, con participantes de 5 a 74 años y cuatro
actividades bien distribuidas (Natación 69, Rehabilitación 63, Hidrogimnasia
62 y Aquagym 56 registros ya deduplicados).

El problema principal no es comercial sino de **calidad de datos**. Un único
valor de **15.000.000** en `ganancias_sector` infló la media de 357.823 a
414.575 (+15,9%) y llevó el coeficiente de asimetría de 0,18 a 15,83. Hay un
salario negativo imposible (−150.000), 33 celdas vacías y dos campos
categóricos con cinco variantes de escritura cada uno, que fragmentaban
cualquier agrupamiento.

Al cruzar por actividad, **Aquagym tiene la mediana salarial más baja
(397.031)**, seguida de Natación (439.541) e Hidrogimnasia (450.654), mientras
Rehabilitación alcanza 471.228: Aquagym queda un **15,7% por debajo** del
mejor posicionado. Por sector, el más bajo es Privado (431.986) y el más alto
Educación (448.940), una brecha moderada del 3,9%. El grupo "Sin dato" muestra
una mediana de 520.045, pero son solo 11 registros: se imputó, no se interpreta.

La tenencia de CUD no explica esa brecha: está entre el 48,2% de Aquagym y el
60,9% de Natación, sin una relación clara con el salario mediano.

## Estrategias propuestas

### 1. Validación en origen de montos

Incorporar reglas de carga que rechacen o marquen `salario <= 0` y
`ganancias_sector > 1.000.000`, con alerta al operador y un campo de
"motivo de corrección".

*Justificación:* con esas dos reglas la media de ganancias vuelve de 414.575
a 357.823 y el coeficiente de asimetría de 15,83 a 0,18. Es la medida de mayor
impacto sobre la confianza de cualquier reporte.

### 2. Estandarización de catálogos e imputación estadística

Aplicar el mapeo de categorías de la Fase 2 (`tiene_cud` → Sí/No;
`identidad_sexual` → Masculino/Femenino/No Binario) ya en el formulario de
carga, usando listas desplegables cerradas. Imputar salario con la mediana por
actividad y dejar constancia con la bandera `salario_imputado`.

*Justificación:* se recuperan las 33 celdas nulas (1,28% del total) y los 2
valores inválidos sin introducir salarios falsos de cero ni separar etiquetas
equivalentes en los `groupby`.

### 3. Revisión del mix de actividades

Aquagym concentra la mediana salarial más baja (397.031) y la menor proporción
de CUD (48,2%). Conviene revisar su estructura de precios/costos y rediseñar
campañas de captación antes de ampliar la oferta, usando Rehabilitación
(471.228 de mediana, el 25% de los participantes) como benchmark interno.

*Justificación:* la brecha del 15,7% entre actividades es la señal más clara
del análisis cruzado y es accionable sin esperar nuevos datos. Debe
reevaluarse con los datos corregidos por las estrategias 1 y 2, que es justo
lo que permite el dataset limpio.
