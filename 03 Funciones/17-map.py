"""
Map
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 12-Jun-2024

Map nos sirve para transformar los elementos de una lista
"""

# Lista
numbers = [1, 2, 3, 4]

# Haciendo otra version de la lista
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i*2)

print(numbers)
print(numbers_v2)

# Haciendo uso de Map y Lambda functions para hacer los mismo (transformar los elementos de la lista)
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)