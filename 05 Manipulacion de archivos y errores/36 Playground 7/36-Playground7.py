"""
Playground 7: Lee un CSV para calcular el total de gastos
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 21-Jun-2024

descripción
"""
import csv

def read_csv(path):
    # Tu código aquí 👇
    total = 0
    with open(path, 'r') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        # total = functools.reduce(lambda acc, row: acc + int(row[1]), reader, 0)
        # el 0 es el iniciador de acc, de esta manera acc inicia como 0 y row parte en el primero item de la lista. Si no acc parte como el primer item de la lista y row como el segundo, y después sigue normal.
        for row in reader:
            total += int(row[1])
    return total

response = read_csv('./Python/Python-CFyME/05 Manipulacion de archivos y errores/36 Playground 7/data.csv')
print(response)