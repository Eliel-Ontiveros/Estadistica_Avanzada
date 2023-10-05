import pandas 
from sklearn import linear_model
import matplotlib.pyplot as plt

datos = pandas.read_csv("Casa.csv")

#print(datos)

datos.columns
datos.shape
x = datos [['Precio de la casa', 'Tamaño (En metros cuadrados)']]
y = datos[['Antiguedad (Years)']]

regr = linear_model.LinearRegression()

regr.fit(x, y)
#print("MODELO", regr.fit)
#predice emision de co2 de un carro de 2300Kg con motor de 1300 cm3

r_sq = regr.score(x, y)
print('cCoeficiente Determinado:', r_sq)
#
print('Intercepcion:', regr.intercept_)
#
print('slope:', regr.coef_)

predictedCo2 = regr.predict([[200000, 50000]])
print("Valor predicho", predictedCo2)

y_pred = regr.predict(x)

errores = y - y_pred

plt.hist(errores, bins=20, edgecolor='k')
plt.xlabel("Error de predicción")
plt.ylabel("Frecuencia")
plt.title("Histograma de Errores de Predicción")

plt.show()