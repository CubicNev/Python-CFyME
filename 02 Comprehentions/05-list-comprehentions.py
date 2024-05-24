"""
List Comprehentions
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 22-Mayo-2024

Sintaxis corta para crear listas a partir de otras colecciones
"""
# Forma tradicional
numbers = []

for element in range(1, 15):
    numbers.append(element)
print(numbers)

# Con list comprehentions
numbers_ch = [element for element in range(1,15)]
print(numbers_ch)

# --- Hacer que cada elemento este multiplicado por dos --- #
# Tradicional
numbers_by2 = []

for element in range(1, 15):
    numbers_by2.append(element*2)
print(numbers_by2)

# Comprehentions
numbers_ch_by2 = [element * 2 for element in range(1,15)]
print(numbers_ch_by2)

# --- Comprehentios con condicionales --- #
# Forma tradicional
pares = []
for i in range(1, 101):
    if i % 2 == 0:
        pares.append(i * 2)
print(pares)

# Comprehentions
pares_ch = [i*2 for i in range(1,11) if i % 2 == 0]
print(pares_ch)