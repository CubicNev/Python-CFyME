"""
Playground 5: Retorna solo palabras de 4 letras y más
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Filtrar una lista de palabras, retornando una lista solo con las que cumplan
con la condición de tener 4 o más letras.
"""
def filter_by_length(words):
    # Escribe tu solución 👇
    return list(filter(lambda word: len(word) > 3, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)