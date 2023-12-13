#Eliel Alfonso Ontiveros Ojeda_368746
#28/11/2023
from scipy.stats import chi2_contingency

datos = [[15, 27], [29, 19]]
chi2_stat, p, dof, _ = chi2_contingency(datos)
alpha = 0.01

print(f"Chi-cuadrado: {chi2_stat}")
print(f"Grados de libertad: {dof}")
print(f"valor de p: {p}")

if p < alpha:
    print("Se rechaza la hipótesis nula")
else:
    print("No se puede rechazar la hipótesis nula")
    
#Chi-cuadrado: 4.526243118294752
#Grados de libertad: 1
#valor de p: 0.03337881746687282
#No se puede rechazar la hipótesis nula