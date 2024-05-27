"""
Funciones
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 27-Mayo-2024

Trabajando con funciones
"""

# Llamada a función print()
print('Hola')

# Ejemplo de creación de función
def my_print():
    print('This is my print')
    print('This is my print 2')

my_print() # Llamada a función

# Función que recibe parámetros, imprime dos veces un mensaje
def imprimeDoble(text):
    print(text * 2)

imprimeDoble("Este es mi texto")
imprimeDoble('Hola')


# Función de suma
def suma(a, b):
    print(a + b) # Suma e imprime

suma(1,1) # 2
suma(1,5) # 6
suma(10,4) # 14

# Usando una función dentro de otra
def sumaExtra(a, b):
    imprimeDoble(a + b)

sumaExtra(2,2)