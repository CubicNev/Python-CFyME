"""
Manejo de archivos 2
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Wed 19-Jun-2024

Se modifica el contenido de un archivo
"""
# Abre archivo con permisos de escritura y lectura, si usas w+ reemplazas el contenido del archivo
with open('./text.txt',  'r+') as file:
    for line in file:
        print(line)
    # Escribe directamente después del último carácter del archivo
    file.write('\nnuevo contenido')
    file.write('\nNUEVO final')