"""
Dictionary Conditional Comprehentions
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 22-Mayo-2024

Sintaxis corta para crear dicionarios con condicionales
"""

import random

contries = ['col', 'mex', 'bol', 'pe']

population = { country:random.randint(1, 100) for country in contries}

print(population) # {'col': 83, 'mex': 35, 'bol': 87, 'pe': 76}

result = { country:totPopulation for (country, totPopulation) in population.items() if totPopulation > 50 }
print(result)

# --- Crear un diccionario con las vocales de la siguiente frase --- #
text = "Hola, soy Nicolas"
unique = { c:c.upper() for c in text if c in 'aeiou'} # {'o': 'O', 'a': 'A', 'i': 'I'}
print(unique)

# Reto en vez de pasar a mayúscula, contar la frecuencia de la letra
print({ c:text.count(c) for c in text if c in 'aeiou' }) # {'o': 3, 'a': 2, 'i': 1}