#random.sample
#Devuelve una lista de k elementos extraídos sin repetición de la secuencia population
import random 
batidoras = range(0,60,1)
print (batidoras)
len(batidoras)
poblacion = list(batidoras)
print(poblacion)
muestra2 = random.sample (poblacion, 12)
print(muestra2) 
batidoras = list(range(0,60,1))
muestra3 = random.sample(list(range(0,60,1)),12)
print(muestra3)

#alturas sin reemplazo
alturas = range(150,200,1)
alturas
len(alturas)
alturas = list(alturas)
alturas_muestra20 = random.sample(alturas,20)
alturas_muestra20
print('Se presentaran las muestras sin reemplazo')
print(alturas_muestra20)

#random.choices
#Genera n muestras a partit de una secuencua con posivilidad de repetición. Muestra con reemplazo
len(alturas)
muestra3 = random.choices(poblacion,k = 40)
muestra3
print('Se presenta la muestra 3 con la función random.choices')
print(muestra3)
muestra4 = random.choices(alturas,k = 20)
print('Se presenta la muestra 4 con la función random.choices')
print(muestra4)
muestra5 = random.choices(alturas,k = 40)
print('Se presenta la muestra 5 con la función random.choices')
print(muestra5)
muestra6 = random.choices(alturas,k = 50)
print('Se presenta la muestra 6 con la función random.choices')
print(muestra6)
 



