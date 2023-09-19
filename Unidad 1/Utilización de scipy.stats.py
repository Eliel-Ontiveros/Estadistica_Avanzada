import scipy.stats as sct
import numpy as np

#Definir los datos de la muestra
muestra_data = np.random.randint(5, 10, 100)

#Crear un Intervalo de Confianza del 90%
#Para la media de la poblacion

loc = np.mean(muestra_data)
scale = sct.sem(muestra_data)
print(sct.norm.interval(confidence =0.90),
              loc,
              scale)
