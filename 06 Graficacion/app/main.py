"""
Archivo principal para graficar crecimiento poblacional de un país
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 26-Jun-2024

Se extrae información de data.csv y se trata la información para graficarla
"""
import utils
import read_csv
import charts

# Reto 1
def run():
    # Se leen datos
    data = read_csv.read_csv('./data.csv')

    # Selecciona país
    country = input(" Type Country: ")

    # Se selecciona la información del país (trae el diccionario)
    result = utils.population_by_country(data, country)

    # Valida que se haya encontrado un resultado
    if len(result) > 0:
        country_res = result[0]
        # Prueba de funcion propia
        # print(utils.get_anual_population(country_res))

        # Extrae la infomación que necesitamos
        labels, values = utils.get_population(country_res)
        # Grafica información
        charts.generate_bar_chart(labels, values)

# Reto 2 (Solución propia)
def pie():
    # Se leen datos
    data = read_csv.read_csv('./data.csv')
    # Se extrae el países y porcentaje de población muldial correspondiente
    labels, values = utils.get_world_population_percentage(data)
    # Grafica de pastel
    charts.generate_pie_chart(labels, values)

# Reto 2 (Solución de clase)
def yourRun():
    # Se leen datos
    data = read_csv.read_csv('./data.csv')
    # Filtrado por contienente
    data = list(filter(lambda country : country['Continent'] == 'South America', data))
    # Trae el nombre del país
    countries = list(map(lambda country: country['Country'], data))
    # Trae los porcentajes de población mundial
    percentages = list(map(lambda percentage: percentage['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
    # Nota se hicieron varias funciones ya que plt.show() detiene el programa
    yourRun()