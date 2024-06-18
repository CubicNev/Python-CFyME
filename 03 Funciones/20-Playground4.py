"""
# Playground 4: Multiplica todos los elementos por dos
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Se usa la función map() y lambdas para transformar una lista de números
"""
def multiply_numbers(numbers):
    # Escribe tu solución 👇
    return list(map(lambda num: num*2, numbers))

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)