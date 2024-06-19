"""
Iterables
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Uso de iterables
"""

# Uso anterior
for i in range(1, 11):
    print(i)

# Veremos qué es un range
my_iter = range(1, 11)
print(my_iter)

# Manejo manual
obj_iter = iter(range(1, 11))
print(obj_iter)
# Iteracion manual:
print(next(obj_iter)) # primer iteracion
print(next(obj_iter)) # segunda iteracion
print(next(obj_iter)) # tercera iteracion
""" Se va generando uno por uno para no ocupar toda la memoria """

# Excediedo memoria
small_iter = iter(range(1,4))
print(next(small_iter))
print(next(small_iter))
print(next(small_iter))
# print(next(small_iter)) # Error
