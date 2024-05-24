"""
Dictionary Comprehentions
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 22-Mayo-2024

Sintaxis corta para crear dicionarios
"""

# --- Creación --- #

# Forma tradicional
diccionario = {}
for i in range(1, 11):
    diccionario[i] = i * 2 # La llave la pone en automatico

print(diccionario) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}

# Comprehentions
diccionario_v2 = { i : i * 2 for i in range(1, 5)}
print(diccionario_v2) # {1: 2, 2: 4, 3: 6, 4: 8}

# --- Ejemplo 1 --- #
import random

contries = ['col', 'mex', 'bol', 'pe']
# Forma tradicional
population = {}

for country in contries:
    population[country] = random.randint(1, 100)
print(population) # {'col': 83, 'mex': 35, 'bol': 87, 'pe': 76}

# Comprehentions
population_v2 = { country:random.randint(1, 100) for country in contries}
print(population_v2) # {'col': 83, 'mex': 35, 'bol': 87, 'pe': 76}

# --- Ejemplo 2 --- #
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

"""
Debe quedar de esta manera:
{
    'nico': 12,
    'zule': 56,
    'santi': 98
}
"""
print(list(zip(names, ages))) # [('nico', 12), ('zule', 56), ('santi', 98)]

new_dict = { name:age for (name, age) in zip(names,ages)}
print(new_dict) # {'nico': 12, 'zule': 56, 'santi': 98}