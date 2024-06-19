"""
Playground 6: Calcular la suma de todas las compras
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Funciones a importar en main.py que sirven para retornar la suma total de ordenes de compra
"""

def get_totals(orders):
    return [order['total'] for order in orders]

def calc_total(totals):
    return sum(totals)