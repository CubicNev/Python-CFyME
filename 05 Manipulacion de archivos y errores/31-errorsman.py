"""
Manejo de errores
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Se hace manejo de errores para que no se detenga el programa
"""

# Generamos errores y los manejamos

try:
    print(0 / 0)
except ZeroDivisionError as error: # Error lanzado por hacer 0/0
    print(error)
    # Buena práctica: Hacer tracking del error

# Con errores propios
try:
    assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as err:
    print(err)

try:
    age = 10
    # Si la edad es menor a 18 lanza un error (Regla de Negocio)
    if age < 18:
        raise Exception('No se permite menores de edad') # Lanzara un error
except Exception as error:
    print(error)

print('Ok!')

# Uniendo to en un solo bloque
try:
    print(0 / 0)

    # No se ejecutan:
    assert 1 != 1, 'Uno no es igual a uno'
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')
except ZeroDivisionError as error: # Error lanzado por hacer 0/0
    print(error)
except AssertionError as err:
    print(err)
except Exception as error:
    print(error)

print('Okey!')