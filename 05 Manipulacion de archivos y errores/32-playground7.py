"""
Playground  7: Captura la excepción: ZeroDivisionError
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Se maneja la excepcion que sale al dividir entre cero dentro de la función my_divide
"""
def my_divide(a, b):
    # Escribe tu solución 👇
    try:
        result = a / b
    except ZeroDivisionError:
        result = 'No se puede dividir por 0'
    return result

response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0
