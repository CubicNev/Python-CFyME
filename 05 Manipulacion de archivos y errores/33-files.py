"""
Manipulación de Archivos 1
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Se lee el archivo de texto plano 'text.txt'
"""

# Abrimos el archivo
file = open("./text.txt")

# Leer todo el archivo
print(file.read())

file.close()

file = open("./text.txt")

# Lectura linea a linea (como iterador)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.close()
file = open("./text.txt")

# Lectura linea a linea con un for
for line in file:
    print(line)

# Cuando se termina de trabajar con el archivo, debe cerrarse para no gastar recursos
file.close()

# Abrir archivos y una vez terminadas las operaciones, cierralo de forma automatoca
with open('./text.txt') as file:
    for line in file:
        print(line)
