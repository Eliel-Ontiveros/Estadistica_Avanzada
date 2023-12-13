import matplotlib.pyplot as plt

# Datos de nicotina
nicotina = [1.09, 1.92, 2.31, 1.79, 2.28, 1.74, 1.47, 1.97,
           0.85, 1.24, 1.58, 2.03, 1.70, 2.17, 2.55, 2.11,
           1.86, 1.90, 1.68, 1.51, 1.64, 0.72, 1.69, 1.85,
           1.82, 1.79, 2.46, 1.88, 2.08, 1.67, 1.37, 1.93,
           1.40, 1.64, 2.09, 1.75, 1.63, 2.37, 1.75, 1.69]

# Crea un histograma
plt.hist(nicotina, bins=7, edgecolor='k', alpha=0.7)
plt.title('Distribución de Nicotina en Cigarrillos')
plt.xlabel('Contenido de Nicotina')
plt.ylabel('Frecuencia')

# Muestra el histograma
plt.show()
