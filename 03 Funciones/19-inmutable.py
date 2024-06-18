"""
Map con inmutabilidad
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Solución a que cuando se modifique o agregue un elemento a un diccionario con map()
no se altere la coleccion original
"""
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

# Agregarle impuestos a los elementos, agregando un atributo

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19 # Aqui
    return new_item

items_w_taxes = list(map(add_taxes, items))
print('Old list:\n', items)
print('New list:\n', items_w_taxes)
