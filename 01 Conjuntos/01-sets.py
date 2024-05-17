"""
Conjuntos
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 17-Mayo-2024

Creación de conjuntos
"""

# import this # Easter Egg!

set_countries = {'col', 'mex', 'bol'}
print(set_countries) # {'mex', 'bol', 'col'}
print(type(set_countries))

# No permite elementos duplicados
set_countries = {'col', 'mex', 'bol', 'bol'}
print(set_countries) # {'mex', 'bol', 'col'}

# Puedes hacer conjuntos de todo tipo de datos
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers) # {1, 2, 443, 23}

set_types = {1, 'hola', False, 12.12}
print(set_types) # {'hola', 1, 12.12, False} (No importa el orden)

# Creando sets a partir de otro elemento
set_from_string = set('hola')
print(set_from_string) # {'l', 'a', 'h', 'o'}

set_from_tuples = set(('abc', 'cvb', 'as', 'abc'))
print(set_from_tuples)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)

# Se puede hacer el proceso a la inversa
unique_numbers = list(set_numbers)
print(unique_numbers)