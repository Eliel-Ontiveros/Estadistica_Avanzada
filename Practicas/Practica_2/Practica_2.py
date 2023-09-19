import pandas as pd
import matplotlib.pyplot as plt

data_dict = {
    'Año': [1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638],
    'Hombres': [5218, 4858, 4422, 4994, 5158, 5035, 5106, 4917, 4703, 5359],
    'Mujeres': [4683, 4457, 4102, 4590, 4841, 4912, 4928, 4783, 4661, 5473]
}

df = pd.DataFrame(data_dict)

plt.figure(figsize=(12, 6))
plt.plot(df['Año'], df['Hombres'], label='Hombres')
plt.plot(df['Año'], df['Mujeres'], label='Mujeres')
plt.xlabel('Año')
plt.ylabel('Nacimientos')
plt.title('Nacimientos de hombres y mujeres a traves de los años')
plt.legend()
plt.show()

df['total_nacimientos'] = df['Hombres'] + df['Mujeres']
df['prop_hombres'] = df['Hombres'] / df['total_nacimientos']
df['prop_mujeres'] = df['Mujeres'] / df['total_nacimientos']
df['comparasion'] = df['prop_hombres'] > df['prop_mujeres']

print(df)