import numpy



#Muestra con 300 alumnos 
print('Se mostraran los calculos con 300 alumnos\n')
cal_300 = numpy.random.randint(0, high = 100, size = 300)
print("Longitud del arreglo", len(cal_300))
print(cal_300)

#Calcular Media
import statistics as st
media_cal_300 = st.mean(cal_300)
print('\nLa media es = ', media_cal_300)

#Calcular Varianza
var_cal_300 = st.variance(cal_300)
print('\nLa varianza es = ', var_cal_300)

#Calcular Desviacion Estandar
import math
des_est_300 = math.sqrt(var_cal_300)
print('\nLa desviacion estandar es = ', round (des_est_300, 2))

#Calcular Intervalo de Confianza
z = 2.575
n_300 = len(cal_300)
int_inf = ((media_cal_300) - (z)*((des_est_300) / (n_300**0.5)))
print('\nEl limite inferior es = ', int_inf)

int_sup = ((media_cal_300) + (z)* ((des_est_300)/(n_300**0.5)))
print('El limite superior es =', int_sup)

rango_mu = int_sup - int_inf
print('El rango de Mu es = ', rango_mu)



#Muestra con 1000 alumnos 
print('\nSe mostraran los calculos con 1000 alumnos\n')
cal_1000 = numpy.random.randint(0, high = 100, size = 1000)
print("Longitud del arreglo", len(cal_1000))
print(cal_1000)

#Calcular Media
import statistics as st
media_cal_1000 = st.mean(cal_1000)
print('\nLa media es = ', media_cal_1000)

#Calcular Varianza
var_cal_1000 = st.variance(cal_1000)
print('\nLa varianza es = ', var_cal_1000)

#Calcular Desviacion Estandar
import math
des_est = math.sqrt(var_cal_1000)
print('\nLa desviacion estandar es = ', round (des_est, 2))

#Calcular Intervalo de Confianza
z = 2.575
n_1000 = len(cal_1000)
int_inf = ((media_cal_300) - (z)*((des_est_300) / (n_1000**0.5)))
print('\nEl limite inferior es = ', int_inf)

int_sup = ((media_cal_300) + (z)* ((des_est_300)/(n_1000**0.5)))
print('El limite superior es =', int_sup)

rango_mu = int_sup - int_inf
print('El rango de Mu es = ', rango_mu)

