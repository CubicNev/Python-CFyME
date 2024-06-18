"""
Reduce
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Función para reducir una coleccion, sacando una "conclusión de la misma"
"""
import functools

numbers = [1, 2, 3, 4]

# Se llama functools y se aplica reduce
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

# Haciendo lo mismo pero con una función
def accum(counter, item):
    print(f" Contador: {counter} Item: {item}")
    return counter + item

result = functools.reduce(accum, numbers)
print(result)