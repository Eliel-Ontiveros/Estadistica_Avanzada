#Eliel Alfonso Ontiveros Ojeda_368746
#28/11/2023
import numpy as np
from scipy.stats import norm, chi2

datos = np.array([23, 60, 79, 32, 57, 74, 52, 70, 82, 36, 80, 77, 81, 95, 41, 65, 92, 85, 55, 76, 52,
                 10, 64, 75, 78, 25, 80, 98, 81, 67, 41, 71, 83, 54, 64, 72, 88, 62, 74, 43, 60, 78,
                 89, 76, 84, 48, 84, 90, 15, 79, 34, 67, 17, 82, 69, 74, 63, 80, 85, 61])

μ  = 65
σ = 21

intervalos = [0, 20, 40, 60, 80, 100]
fobser, bordes = np.histogram(datos, bins=intervalos)

prob_acum = np.diff(norm.cdf(bordes, loc=σ, scale=μ))
fesperadas =  len(datos) * prob_acum

#formula para chi2
chic2 = np.sum((fobser - fesperadas)**2 / fesperadas)
glibertad = len(intervalos) - 2

valor_critico = chi2.ppf(0.95, glibertad)


print(f"Frecuencias observadas: {fobser}")
print(f"Frecuencias esperadas: {fesperadas}")
print(f"chi-cuadrado: {chic2}")
print(f"Grados de libertad: {glibertad}")
print(f"Valor crítico de chi^2: {valor_critico}")

if chic2 > valor_critico:
    print("Rechazamos la hipótesis nula")
else:
    print("No hay suficiente evidencia para rechazar la hipótesis nula. No hay diferencias significativas")

#resultados
    
#Frecuencias observadas: [ 3  5  9 25 18]
#Frecuencias esperadas: [7.23265052 7.26669855 6.64635427 5.53396279 4.19464129]
#chi-cuadrado: 117.92651670285937
#Grados de libertad: 4
#Valor crítico de chi^2: 9.487729036781154
#Se rechazó la hipótesis 

