import numpy as np
import matplotlib.pyplot as plt

# Tus datos
x = np.array([10, 10, 10, 10, 10, 50, 50, 50, 50, 50])
y = np.array([13, 18, 16, 15, 20, 86, 90, 88, 88, 92])

m, b = np.polyfit(x, y, 1)

x_line = np.linspace(min(x), max(x), 100)

y_line = m * x_line + b

# Crea la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Datos originales')
plt.plot(x_line, y_line, '-', label='Línea de regresión')
plt.xlabel('Presión')
plt.ylabel('Lectura correspondiente')
plt.title('Regresión lineal')
plt.legend()
plt.show()

lectura = 54
presion_estimada = (lectura - b) / m

print(f"La presión estimada para una lectura de {lectura} es {presion_estimada}")
