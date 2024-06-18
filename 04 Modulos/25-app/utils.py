"""
Utilidades (Ejemplo de módulo)
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Se tienen funcionalidades parra usar luego
"""
def get_population():
    keys = ['col', 'bol']
    values = [300, 400]

    return keys, values

# Obtener la información de un país en especifico, dada una lista de países (lista de diccionarios)
def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
