#Encuentre una proporcion de la poblacion y la muestra
#¿Con que certeza podemos afirmar que la poblacion se va a comportar igual que la muestra?
text = "txt"
repeated = text * 4
print("repeated\n")


unos = [1]
no_def = (unos * 9990)
print(no_def)
print(type(no_def))
print(len(no_def))


ceros = [0]
defect = (ceros * 100)
print(defect)
print(type(defect))
print(len(defect)) 


poblaciones = (defect + no_def)
print(len(poblaciones))
print(type(poblaciones))
print(poblaciones)


import random
random.shuffle(poblaciones)
print(poblaciones)


#Muestra de tamaño 1000 de la poblacion
muestra_1 = random.sample(poblaciones, 1000)
print(muestra_1)


#Contar el numero de unos con Count
unos_m1 = muestra_1.count(1)
print(unos_m1)


#Contar el numero de ceros con Count
ceros_m1 = muestra_1.count(0)
print(ceros_m1)


#Muestra el porcentaje de defectuosos entre la poblacion
proporcion_def = ceros_m1 / len(poblaciones)
print(proporcion_def)


#Muestra de tamaño 1000 de la poblacion
muestra_2 = random.sample(poblaciones, 1000)
print(muestra_2)


#Contar el numero de unos con Count
unos_m2 = muestra_2.count(1)
print(unos_m1)


#Contar el numero de ceros con Count
ceros_m2 = muestra_2.count(0)
print(ceros_m2)


#Muestra el porcentaje de defectuosos entre la poblacion
proporcion_def_2 = ceros_m2 / len(poblaciones)
print(proporcion_def_2)


#Muestra de tamaño 1000 de la poblacion
muestra_3 = random.sample(poblaciones, 1000)
print(muestra_3)


#Contar el numero de unos con Count
unos_m3 = muestra_3.count(1)
print(unos_m3)


#Contar el numero de ceros con Count
ceros_m3 = muestra_3.count(0)
print(ceros_m3)


#Muestra el porcentaje de defectuosos entre la poblacion
proporcion_def_3 = ceros_m3 / len(poblaciones)
print(proporcion_def_3)


#Muestra de tamaño 1000 de la poblacion
muestra_4 = random.sample(poblaciones, 1000)
print(muestra_4)


#Contar el numero de unos con Count
unos_m4 = muestra_4.count(1)
print(unos_m4)


#Contar el numero de ceros con Count
ceros_m4 = muestra_4.count(0)
print(ceros_m4)


#Muestra el porcentaje de defectuosos entre la poblacion
proporcion_def_4 = ceros_m4 / len(poblaciones)
print(proporcion_def_4)


#Muestra de tamaño 1000 de la poblacion
muestra_5 = random.sample(poblaciones, 1000)
print(muestra_5)


#Contar el numero de unos con Count
unos_m5 = muestra_5.count(1)
print(unos_m5)


#Contar el numero de ceros con Count
ceros_m5 = muestra_5.count(0)
print(ceros_m5)


#Muestra el porcentaje de defectuosos entre la poblacion
proporcion_def_5 = ceros_m5 / len(poblaciones)
print(proporcion_def_5)








