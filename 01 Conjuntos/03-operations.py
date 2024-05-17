"""
Operaciones de conjuntos
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 17-Mayo-2024

Operaciones de conjuntos
"""

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Join o union de conjuntos
set_c = set_a.union(set_b)
print(set_c) # {'bol', 'mex', 'col', 'pe'}
# Alternativa
print(set_a | set_b) # {'bol', 'mex', 'col', 'pe'}

# Interseccion: Cuáles son los elementos en común
set_c = set_a.intersection(set_b)
print(set_c) # {'bol'}
# Alternativa
print(set_a & set_b) # {'bol'}

# Diferencia: Quita los elementos de un conjunto en otro
set_c = set_a.difference(set_b)
print(set_c) # {'mex', 'col'}
print(set_a - set_b) # {'mex', 'col'}

# Diferencia simetrica: Hacer una union sin los elementos en común
set_c = set_a.symmetric_difference(set_b)
print(set_c) # {'pe', 'mex', 'col'}
print(set_a ^ set_b) # {'pe', 'mex', 'col'}