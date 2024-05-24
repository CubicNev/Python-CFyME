"""
List Comprehentions: Reto
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 24-Mayo-2024

Resolviendo reto de hacer una lista con las coordenadas delimitadas por un cubo de dimensiones x, y, z
cuya suma de los componentes i,j,k sea diferente de n. Haciendo uso de list comprehentions.
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Solucion 1:

xs = [i for i in range(0,x+1)]
ys = [j for j in range(0,y+1)]
zs = [k for k in range(0,z+1)]

coordenadas = [[i, j, k] for i in xs for j in ys for k in zs if i+j+k != n]
print(coordenadas)

# Solucion 2 (más optima):
# print( [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)])
solucion = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(solucion)
