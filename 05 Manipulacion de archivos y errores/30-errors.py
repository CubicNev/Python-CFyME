"""
Errores de python
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Algunos ejemplos de errores que se presentan en python
"""
# print(0/0)) # SyntaxError: unmatched ')'
# print(0/0) # ZeroDivisionError: division by zero
# print(inexistente) # NameError: name 'inexistente' is not defined

suma = lambda x,y: x + y
# Assert funciona para verificar
assert suma(2,2) == 4 # No causa error, al 'verificar' todo paso de forma correcta

suma_fail = lambda x,y: x + (y * 2)
# assert suma_fail(2,2) == 4 # AssertionError
""" Inicio de pruebas unitarias, assert sirve para hacerlas """

# Lanzando excepciones propias
age = 10
# Si la edad es menor a 18 lanza un error (Regla de Negocio)
if age < 18:
    #raise Exception('No se permite menores de edad') # Lanzara un error
    pass