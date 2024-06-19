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

# assert 1 != 

print('Ok!')