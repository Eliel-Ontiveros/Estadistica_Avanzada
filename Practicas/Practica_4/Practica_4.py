import numpy as np
from statsmodels.stats.proportion import proportion_confint

count_houses_with_tv = 275
total_houses = 500

conf_interval = proportion_confint(count=count_houses_with_tv, nobs=total_houses, alpha=0.1, method='normal')

print("90% intervalo de confianza por la proporcion de casas con 2 o mas televisores:")
print(conf_interval)