"""
Leer CSV
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 21-Jun-2024

Se lee un archivo CSV para procesar la información que contiene.
world_population.csv: Rank (Rango del país), CCA3 (Abreviatura), Country, Capital, Continent, 2022 Population, 2020, 2015, 2010, 1990, 1970,
Area (km2), Density, World Population Percetage

Se lee y procesa información para seleccionar un país y graficar su información

"""
import csv

# Función para leer el archivo
def read_csv(path):
    # Se abre con modo lectura
    with open(path, 'r', encoding='UTF-8') as csvfile:
        # Lector recibe el archivo y el tipo de delimitador que usa
        reader = csv.reader(csvfile, delimiter=',')
        # Se extraen los encabezados
        header = next(reader)
        # Lista para guardar los diccionarios generados
        data = []
        # Iteración que lee fila por fila
        for row in reader:
            # Union de encabezado con fila en una lista de tuplas: (columna, valor)
            iterable = zip(header, row)
            # Se pasa a diccionario
            country_dict = {key: value for key, value in iterable}
            # Se agrega el diccionario a la lista
            data.append(country_dict)
        return data

# Correr el archivo como script
if __name__ == '__main__':
    data = read_csv('c:/Users/bc.jnevarez/Codigo/Python/Python-CFyME/05 Manipulacion de archivos y errores/35-app-readcsv/data.csv')
    print(data[0])