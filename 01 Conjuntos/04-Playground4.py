"""
Playground 1: Elimina elementos duplicados usando conjuntos
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 20-Mayo-2024

Debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set
"""
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = countries | northAm | centralAm | southAm

print(new_set)
