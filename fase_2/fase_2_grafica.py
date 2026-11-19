import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df3 = pd.read_csv('../fase_1/proyecto_3_todos_al_agua_limpio_fase1.csv')

# Definir estilo
sns.set_theme(style="whitegrid")

# 1. Histograma / Densidad con KDE para ganancias_sector y salario
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.histplot(df3['ganancias_sector'].dropna(), kde=True, ax=axes[0], color='teal', bins=30)
axes[0].set_title('Distribución de Ganancias por Sector', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Ganancias Sector', fontsize=12)
axes[0].set_ylabel('Frecuencia', fontsize=12)

sns.histplot(df3['salario'].dropna(), kde=True, ax=axes[1], color='coral', bins=30)
axes[1].set_title('Distribución de Salarios', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Salario', fontsize=12)
axes[1].set_ylabel('Frecuencia', fontsize=12)

plt.tight_layout()
plt.savefig('distribucion_financiera.png', dpi=300)
plt.close()

# 2. Boxplot comparativo por Actividades
plt.figure(figsize=(10, 6))
sns.boxplot(data=df3, x='actividades', y='salario', palette='Set2')
plt.title('Diagrama de Caja de Salarios por Actividad', fontsize=14, fontweight='bold')
plt.xlabel('Actividad', fontsize=12)
plt.ylabel('Salario', fontsize=12)
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('boxplot_salario_actividades.png', dpi=300)
plt.close()

# 3. Scatterplot con hue (ej. edad vs salario con hue por actividades o sectores)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df3, x='edad', y='salario', hue='actividades', palette='deep', alpha=0.8, s=70)
plt.title('Relación entre Edad y Salario según Actividad', fontsize=14, fontweight='bold')
plt.xlabel('Edad (años)', fontsize=12)
plt.ylabel('Salario', fontsize=12)
plt.legend(title='Actividades', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('scatterplot_edad_salario.png', dpi=300)
plt.close()

# Mensaje de confirmacion
print("Gráficos generados y guardados exitosamente a 300 DPI.")