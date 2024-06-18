"""
Módulos
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Ejemplo de módulo
"""
# Para obtener información del sistema
import sys

print(sys.path)

# Para expresiones regulares
import re
text = "Mi numero de teléfono es 311 123 121, el código del país es 57, mi número de la suerte s 3"
# Se puee crear una expresión regular para obtener solo los strings que coincidan con lo que es un númerod entro del texto
result = re.findall('[0-9]+', text)
print(result)

# Para manejo de horas y fechas
import time
timestamp = time.time()
local = time.localtime()
format_local = time.asctime()
print(timestamp)
print(format_local)

# Utilidad para manejar listas
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
# Frecuencia de un número en la lista
counter = collections.Counter(numbers)
print(counter)

import platform
print(dir(platform))