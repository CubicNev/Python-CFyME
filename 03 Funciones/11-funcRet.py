"""
Parámetros por defecto y múltiples returns
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 06-Junio-2024

Se ve más a profundidad las funciónes
"""

# Forma tradiconal

def find_volume(length, width, depth): return length * width * depth

result = find_volume(10, 20, 3)

print(result)

# Parámetros por defecto

def find_volume_default(length = 1, width=1, depth=1): return length * width * depth

result1 = find_volume_default()

print(result1)

result2 = find_volume_default(width=10)

print(result2)

# Retornando multiples valores

def find_volume_doble(length = 1, width=1, depth=1): return length * width * depth, width, "Ejecucion exitosa"

resultados = find_volume_doble(width=13) # regresa una tupla
print(resultados)
print(resultados[0])

volumen, ancho, mensaje = find_volume_doble(width=9, length=2)
print(volumen)
print(ancho)
print(mensaje)