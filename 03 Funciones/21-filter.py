"""
Filter
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Filter filtra elementos de una lista
"""

numbers = [1,2,3,4,5]

# Da elementos pares dentro de la lista
filter_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filter_numbers)
