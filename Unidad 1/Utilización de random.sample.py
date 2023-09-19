#Primero se identifican los clientes del 1 al 1000
#Inciso a)
import random
clientes = random.sample(range(1,1000),100)
print('Se clasifican 100 clientes entre los 1000 clientes totales')
print(clientes)

#Inciso b)
clientes_1 = random.sample(range(1,800),80)
print('Se eligen 80 clientes caucásicos entre los 800 que son')
print(clientes_1)
clientes_2 = random.sample(range(801,950),15)
print('Se eligen 15 clientes afroamericanos entre los 150 que son')
print(clientes_2)
clientes_3 = random.sample(range(951,1000),5)
print('Se eligen 5 clientes hispanoamericanos entre los 50 que son')
print(clientes_3)
clientes = clientes_1 + clientes_2 + clientes_3
print('Se muestran los clientes que se seleccionaron entre los 3 tipos anteriores')
print(clientes)