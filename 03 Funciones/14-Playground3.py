"""
Playground 3: Tienda de Tecnología
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Mon 10-Jun-2024

Ejercicio con funciones
"""
def message_creator(text):
    # Escribe tu solución 👇
    if text == 'computadora':
        return 'Con mi computadora puedo programar usando Python'
    elif text == 'celular':
        return 'En mi celular puedo aprender usando la app de Platzi'
    elif text == 'cable':
        return '¡Hay un cable en mi bota!'
    else:
        return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)