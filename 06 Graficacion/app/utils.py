"""
Utilidades para manejar datos poblacionales obtenidos de data.csv
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 26-Jun-2024

Se tienen funcionalidades para usar luego
"""
# Para enviar datos de crecimiento poblacional a gráfica de barras
# Entrada: País seleccionado en forma de diccionario
def get_population(country_dict):
    # Seleccion manual
    population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

# Obtener la información de un país en especifico, dada una lista de países (lista de diccionarios)
def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
