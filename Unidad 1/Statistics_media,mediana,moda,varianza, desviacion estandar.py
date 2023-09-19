import numpy
c_100 = numpy.random.randint(0, high = 100, size = 100)
print("Longitud del arreglo", len(c_100))
print(c_100)


import statistics as st

#Media de Statistics
media_c100 = st.mean(c_100)
print("La media de las calificaciones es = ", media_c100, "\n")


#Desviacion estandar
ds_c_100 = st.stdev(c_100)
print("La desviacion estandar de las calificaciones es = ", ds_c_100, "\n")


#Varianza
var_c_100 = st.variance(c_100)
print("La varianza de las calificaciones es = ", var_c_100, "\n")


#Mediana
mediana_c_100 = st.median(c_100)
print("La mediana de las calificaciones es = ", mediana_c_100, "\n")


#Moda
moda_c_100 = st.mode(c_100)
print("La moda de las calificaciones es = ", moda_c_100, "\n")

