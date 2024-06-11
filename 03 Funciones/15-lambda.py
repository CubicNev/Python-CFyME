"""
Funciones lambda
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Mon 10-Jun-2024

Uso de lambdas, ejemplo con dos funciónes que hacen exactamente lo mismo.
"""

'''
Función que incrementa un valor
Entrada: x
Salida: x + 1
'''
# Función tradicional
def incrementa(x):
    return x + 1

# Función lambda
incrementaLmd = lambda x : x + 1

result = incrementa(10)
print(result)

result = incrementaLmd(20)
print(result)


'''
Función lambda que recibe más de un argumento, imprime el nombre completo con mayusculas
Entrada: nombre, apellidos
Salida: Nombre completo con formato
'''
full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)