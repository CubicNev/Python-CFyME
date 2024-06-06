"""
Funciones con return
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 06-Junio-2024

Se hace uso de la palabra clave return para que las funciones den valores de
salida.
"""

""" Anteriormente se hacia
sum = 0
for x in range(1, 10):
    sum += x
print(sum) # 42
"""

# Para sumar valores dentro de un rango
def sum_with_range(min, max):
    sum = 0
    for x in range(min, max): sum += x
    return sum

result1 = sum_with_range(1, 10)
print(result1)
result2 = sum_with_range(20, 30)
result3 = sum_with_range(1, 100)

result = sum_with_range(result1, result1 + 10)
print(result)
