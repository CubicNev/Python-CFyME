"""
Archivo principal
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Este archivo importa las utilidades de utils.py
"""
import utils

keys, values = utils.get_population()
print(keys,values)

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

country = input(" Type Country: ")

result = utils.population_by_country(data, country)
print(result)
