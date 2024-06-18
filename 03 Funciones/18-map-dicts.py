"""
Map con diccionarios
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Se hacen transformaciónes de diccionarios usando map()
"""
# Lista de diccionarios
items = [
    {
        'producto': 'camisa',
        'price': 100
    },
    {
        'producto': 'pantalones',
        'price': 300
    },
    {
        'producto': 'shorts',
        'price': 200
    }
]

# Quiero una lista con precios
prices = list(map(lambda item: item['price'], items))
print(prices)

# Agregarle impuestos a los elementos, agregando un atributo

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

items_w_taxes = list(map(add_taxes, items))
print(items)
print(items_w_taxes)
