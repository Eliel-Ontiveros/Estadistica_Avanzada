import pandas 
from sklearn import linear_model

datos = pandas.read_csv("cars.csv")

#print(datos)

datos.columns
datos.shape
x = datos[[ 'Weight' , 'Volume' ]]

y = datos['CO2']

regr = linear_model.LinearRegression()

regr.fit(x, y)
#print("MODELO", regr.fit)
#predice emision de co2 de un carro de 2300Kg con motor de 1300 cm3

r_sq = regr.score(x, y)
print('coefficient of determination:', r_sq)
#
print('intercept:', regr.intercept_)
#
print('slope:', regr.coef_)

predictedCo2 = regr.predict([[2300, 1300]])
print("Valor predicho", predictedCo2)