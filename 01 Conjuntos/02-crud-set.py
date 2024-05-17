"""
Modificando conjuntos
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 17-Mayo-2024

Operaciones para modificar conjuntos
"""

set_countries = {'col', 'mex', 'bol'}

# Consultas

size = len(set_countries)
print(size) # 3

print('col' in set_countries) # True
print('pe' in set_countries) # False

# Altas (add)

set_countries.add('pe')
print(set_countries) # {'pe', 'mex', 'bol', 'col'}
set_countries.add('pe') # Se mantintienen la propiedad de elementos unicos
print(set_countries) # {'pe', 'mex', 'bol', 'col'}

# Actualizaciones (update): Sumas conjuntos

set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries) # {'pe', 'bol', 'ecua', 'ar', 'mex', 'col'}

# Bajas (remove)
set_countries.remove('col')
print(set_countries) # {'ecua', 'arg', 'pe', 'mex', 'bol'}

# set_countries.remove('col') # Eliminar un elemeto que no existe # Error

# Hacer eliminaciones de forma segura
set_countries.remove('ar')
set_countries.discard('arg')
print(set_countries) # {'mex', 'bol', 'pe', 'ecua'}

set_countries.add('arg')
print(set_countries) # {'arg', 'mex', 'bol', 'pe', 'ecua'}

# Vaciar el set

set_countries.clear()
print(set_countries) # set()
print(len(set_countries)) # 0

