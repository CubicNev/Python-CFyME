"""
Playground 2: Crea una lista usando List Comprehension
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 22-Mayo-2024

"""
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [ number for number in numbers if number % 2 == 0 ]

print('v2 =>', even_numbers_v2)