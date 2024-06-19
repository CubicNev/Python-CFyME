"""
Playground 6: Calcular la suma de todas las compras
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Arhivo main.py de playground que usa funciones de my_functions.py
"""

import my_functions, functools

def get_total(orders):
    # Tu código aquí 👇
    totales = my_functions.get_totals(orders)
    # print(totales)
    return my_functions.calc_total(totales)

# Solucion alternativa (No sigue indicaciones xd)
def get_total_fast(orders):
    return functools.reduce(lambda contador, order: contador + order['total'], orders, 0)

orders = [
    {
        "customer_name": "Nicolas",
        "total": 100,
        "delivered": True,
    },
    {
        "customer_name": "Zulema",
        "total": 120,
        "delivered": False,
    },
    {
        "customer_name": "Santiago",
        "total": 20,
        "delivered": False,
    }
]

total = get_total(orders)
print(total)
print(get_total_fast(orders))