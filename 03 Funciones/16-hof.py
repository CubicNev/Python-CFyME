"""
Higher Order Fuction
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 11-Jun-2024

Usando funciones como argumentos
"""
# Función que recibe un parametró
def increment(x):
    # lo modifica, y lo returnea xd
    return x + 1

# Recibe un parametro y la declaración de una función (que se va a ejecutar)
def high_ord_func(x, func):
    # Retorna la suma de x con lo que haga al ejecutar la función con x
    return x + func(x)

# No se pone increment() porque estaríamos ejecutando la función
result = high_ord_func(2, increment) # Se envía solo la definición de la función
print(result) # 2 + (2 + 1)

'''
Beneficio de HOF: La estructura se acorta con lambdas y se agrega modularidad
'''
incrementLmd = lambda x : x + 1

high_ord_func_lmd = lambda x, func : x + func(x)

result = high_ord_func_lmd(2, incrementLmd)
print(result)
# Se agrego moludaridad, y ahora podemos enviar cualquier función que queramos para modificar x
result = high_ord_func_lmd(2, lambda x : x + 2)
print(result)
result = high_ord_func_lmd(2, lambda x : x * 5)
print(result)
