import numpy as np
import matplotlib.pyplot as plt

x = [28, 8, 11, 37, 15, 25, 51, 11, 32, 34, 43, 2, 40, 16, 40, 25, 40, 17, 21, 57]
y = [8, 8, 9, 72, 22, 51, 85, 4, 75, 48, 72, 1, 62, 37, 75, 42, 75, 47, 57, 95]

plt.scatter(x, y)
model = np.polyfit(x, y, 9)

print('Modelo Lineal', model)


#Prediccion utilizando poly1d()

predict = np.poly1d(model) #Predict va a contener los coeficientes 

x_value = 20
predict(x_value) #Evaluar el modelo para x = x_value

#Exactitud del modelo R-Squared
#Se debe importar sklearn.metric import r2_score

from sklearn.metrics import r2_score 
r2 = r2_score(y, predict(x))

print('El valor de r_square es', r2)

#Dibujando el Modelo

x_axis = range(0,60)
y_axis = predict(x_axis)
plt.scatter(x,y)
plt.plot(x_axis, y_axis, c = 'g')

## Aqui termina el Ejercicio ##

my_model = np.poly1d(np.polyfit(x, y, 3))

print('Mi modelo', my_model)
predict = np.poly1d(my_model)

x_value = 20
x_20 = predict(x_value)

print('Valor de y para x = 20 es = ', x_20)