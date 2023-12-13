#Eliel Alfonso Ontiveros Ojeda_368746
#28/11/2023

import numpy as np
from scipy.stats import f_oneway

# Datos
A = np.array([5.2, 4.7, 8.1, 6.2, 3.0])
B = np.array([9.1, 7.1, 8.2, 6.0, 9.1])
C = np.array([3.2, 5.8, 2.2, 3.1, 7.2])
D = np.array([2.4, 3.4, 4.1, 1.0, 4.0])
E = np.array([7.1, 6.6, 9.3, 4.2, 7.6])

# Realizar el análisis de varianza (ANOVA)
statistic, p_value = f_oneway(A, B, C, D, E)

# Nivel de significancia
alpha = 0.05

# Imprimir resultados
print("Estadístico de prueba (F):", statistic)
print("Valor p:", p_value)

# Tomar decisiones basadas en el valor p
if p_value < alpha:
    print("Rechazamos la hipótesis nula. Hay evidencia suficiente para decir que las cinco marcas no proporcionan el mismo número medio de horas de alivio.")
else:
    print("No hay suficiente evidencia para rechazar la hipótesis nula. No hay diferencias significativas en el número medio de horas de alivio proporcionadas por las cinco marcas.")

#Estadístico de prueba (F): 6.5865080964859235
#Valor p: 0.001497104486931074
#Rechazamos la hipótesis nula. Hay evidencia suficiente para decir que las cinco marcas no proporcionan el mismo número medio de horas de alivio.