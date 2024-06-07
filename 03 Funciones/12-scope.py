"""
Scope
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 07-Jun-2024

Se trabaja sobre el Scope de python
"""
# Variable con alcance global: se puede utilizar en todo el archivo
price = 100

def increment():
    # Variable con alcance local
    price = 200
    result = price + 10
    print(result)
    return result

print(price)
price_2 = increment() # El price de la funcion (local) es diferente al price global
print(price_2)

# print(result) # Error: La variable solo esta definida dentro de la función increment()
