"""
Archivo principal
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Este archivo importa las utilidades de utils.py
"""
import utils

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

# Fucnión que controla la ejecución
def run():
    keys, values = utils.get_population()
    print(keys,values)

    country = input(" Type Country: ")

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()