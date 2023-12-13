#Eliel Alfonso Ontiveros Ojeda_368746
#Examen Parcial 2

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("heart_data.csv")

X = df[["biking", "smoking"]]
y = df["heart.disease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio: {mse}")

coefficients = model.coef_
print(f"Coeficientes del modelo: {coefficients}")

intercept = model.intercept_
print(f"Intercepto del modelo: {intercept}")

mean_biking = df["biking"].mean()
mean_smoking = df["smoking"].mean()

input_data = pd.DataFrame({"biking": [mean_biking], "smoking": [mean_smoking]})

model = LinearRegression()

X = df[["biking", "smoking"]]
y = df["heart.disease"]
model.fit(X, y)

prediction = model.predict(input_data)

print(f"Proyección o pronóstico para la media de las variables independientes: {prediction[0]}")

#RESULTADOS#
#Error cuadrático medio: 0.4522479816837186
#Coeficientes del modelo: [-0.20076448  0.17827087]
#Intercepto del modelo: 15.01718202777425
#Proyección o pronóstico para la media de las variables independientes: 10.17453806810241