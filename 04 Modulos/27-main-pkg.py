"""
Paquetes
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Ejemplifica el uso de paquetes, usando los módulos de 'pkg'
"""
# Sintaxis alternativa de importacion

# Importando funciones del modulo 1
from pkg.mod_1 import func_1, func_2

# Importando funciones del modulo 2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())

import pkg
print(pkg.URL)
print(pkg.mod_1.func_1())