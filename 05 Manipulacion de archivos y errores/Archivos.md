# Manipulación de archivos

Python permite la lectura y escritura de distintos archivos (por ejemplo los `.txt`)

## Abrir un archivo

Hay dos formas. La primera consiste en usar la función `open(file)` para almacenar el archivo en una variable y tabajar sobre el usando esa variable, en este caso es recomendable usar la función `close()` cuando se termine de trabajar en el archivo para no usar tantos recursos.

```python
# Abrimos el archivo
file = open("./text.txt")
# Cuando se termina de trabajar con el archivo, debe cerrarse para no gastar recursos
file.close()
```

La segunda forma se hace con el comando `with`, permitiendo que se ejecute un bloque de codigo para manipular el archivo y una vez termine, este se cierre de forma automatica sin tener que usar `close()`

```python
with open('./text.txt') as file:
    # Leer archivo linea a linea
    for line in file:
        print(line)
```

> ⚠️ **Cuidado:** Al usar `open()` por defecto solo viene con permisos de lectura.

La función `open()` toma dos parámetros: `filename` y `mode` Existiendo cuatro formas de abrir un archivo.

1. `r` (**read**). Es el valor por defecto. Abre el archivo para leerlo, manda error si el archivo no existe.
2. `a` (**append**). Abre el archivo para agregarle contenido, crea el archivo si no existe.
3. `w` (**write**). Abre el archivo para escribir, crea el archivo si no existe.
4. `x` (**create**) Crea el archivo especificado, regresa un error si el archivo no existe.

Adicionalmente puedes específicar si el archivo debe manejare como un binario o como texto plano:

- `t` (**text**). Modo por defecto, abre en modo de texto plano.
- `b` (**binary**). Abre en modo binario (ej. imagenes)

Cuando se abre un archivo, sin especificar un modo, por default se ejecutaría asi

```python
f = open("demofile.txt", "rt") # Abre como texto plano en modo lectura
```

> Más información sobre los permisos: [Permisos en linux][2], [Administración de usuarios][3]. Fuente [aqui][4].

## Leer un archivo

Hay varias funciones: `read()` lee todo el archivo de una sola vez, `readline()` lee una línea a la vez funcionando como un iterador, también podemos leerlo recorriendolo con un `for` a manera de iterable.

```python
# Leer todo el archivo
print(file.read())

# Lectura linea a linea (como iterador)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# Lectura linea a linea con un for (iterable)
for line in file:
    print(line)
```

## Modificar un archivo

Para escribir se usa `open()` con los parametros `a` (*append*, agrega contenido al final del archivo, también hce lo mismo `r+`) o `w` (*write*, va a **sobreecribir** el contenido existente).

```python
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# r+ para permisos tanto de lectura como de escritura. Enfocado en agregar nuevo contenido al contenido existente en el archivo

# w+ para permisos tanto de lectura como de escritura. Enfocado en reescribir el contenido existente
```

> Más info sobre manejo de archivos [aqui][1]

## Archivos CSV

Son archivos que almacenan información en filas y columnas. Los ocupan en todo tipo de areas: finanzas, data science, etc. Normalmente se procesan y analizan.

Plataforma para ciencia de datos, tiene varios datasets para poder procesar: [Kaggle](https://www.kaggle.com/)

Por ejemplo, se usa [World Population Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset)

Para leerlo se debe importar el módulo `csv`

```python
import csv
```

Para modularidad y facilidad se puede crear una función para leer el archivo.

```python
# Función para leer el archivo
# Param: ruta del archivo
def read_csv(path):
    # Se abre con modo lectura
    with open(path, 'r') as csvfile:
        # Lector recibe el archivo y el tipo de delimitador que usa
        reader = csv.reader(csvfile, delimiter=',')
        # Iteración que lee fila por fila
        for row in reader:
            print('***' * 5)
            print(row)
```

> ⚠️ **Cuidado:** El delimitador que se indica en la función `reader(file, delimter)` depende de cuál use el archivo.

La función `read_csv(path)` imprime las filas en forma de listas de datos, pero es más util si se tuviera cada fila en forma de diccionarios donde la clave es el nombre (encabezado) de la columna.

```python
***************
['80', 'BOL', 'Bolivia', 'Sucre', 'South America', '12224110', '11936162', '11090085', '10223270', '8592656', '7096194', '5736088', '4585693', '1098581', '11.1272', '1.012', '0.15']
***************
['28', 'COL', 'Colombia', 'Bogota', 'South America', '51874024', '50930662', '47119728', '44816108', '39215135', '32601393', '26176195', '20905254', '1141748', '45.4339', '1.0069', '0.65']
***************
```

## Reto: Pasar lista a diccionario

Transformar la fila leía a formato de diccionario para que su lectura sea más cómoda. De tal forma que tengamos una lista de diccionarios,*i.e.*

```python
[
    {
        'Country': 'Colombia',
        'Capital': 'Bogota',
        '2022 Population': 3000,
        'World Population Percentagel': 0.12
    },
    {
        'Country': 'Bolivia',
        'Capital': 'Sucre',
        '2022 Population': 500,
        'World Population Percentagel': 0.12
    }
]
```

Recordando que el `reader` es un Iterable, por lo que va a tomar es la primer fila, donde viene el nombre de las columnas.

```python
# Lector recibe el archivo y el tipo de delimitador que usa
reader = csv.reader(csvfile, delimiter=',')
# Se extraen los encabezados
header = next(reader)
```

Entonces tenemos una lista con el nombre de las columnas, podemos utilizar la función `zip()` para unir el encabezado con la fila. Recordando que `zip()` da un iterable, que es una lista de tuplas.

```python
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Se extraen los encabezados
        header = next(reader)
        for row in reader:
            # Union de encabezado con fila en una lista de tuplas: (columna, valor)
            iterable = zip(header, row)
```

```python
print(list(iterable))

...
[('Rank', '78'), ('CCA3', 'BDI'), ('Country/Territory', 'Burundi'), ('Capital', 'Bujumbura'), ('Continent', 'Africa'), ('2022 Population', '12889576'), ('2020 Population', '12220227'), ('2015 Population', '10727148'), ('2010 Population', '9126605'), ('2000 Population', '6307659'), ('1990 Population', '5483793'), ('1980 Population', '4312834'), ('1970 Population', '3497834'), ('Area (km²)', '27834'), ('Density (per km²)', '463.0874'), ('Growth Rate', '1.027'), ('World Population Percentage', '0.16')]
```

Ahora se crea un diccionario usando *dictionary comprehention* a partir del iterable.

```python
country_dict = {key: value for key, value in iterable}
```

Itera obteniendo los pares clave-valor que estan en el `iterable` generado anteriormente.

```python
print(country_dict)

...
{'Rank': '74', 'CCA3': 'ZWE', 'Country/Territory': 'Zimbabwe', 'Capital': 'Harare', 'Continent': 'Africa', '2022 Population': '16320537', '2020 Population': '15669666', '2015 Population': '14154937', '2010 Population': '12839771', '2000 Population': '11834676', '1990 Population': '10113893', '1980 Population': '7049926', '1970 Population': '5202918', 'Area (kmÂ²)': '390757', 'Density (per kmÂ²)': '41.7665', 'Growth Rate': '1.0204', 'World Population Percentage': '0.2'}
```

O podrias usar el método que ya lee todo como un diccionario.

```python
fileCSV = csv.DictReader(file, delimiter=',')
```

<!-- Referencias -->

[1]: <https://realpython.com/working-with-files-in-python/> "Working With Files in Python"
[2]: <https://platzi.com/blog/cosas-que-nos-sabias-sobre-el-sistema-de-permisos-de-linux-realmente-es-octal/> "¡Cosas que nos sabías sobre el sistema de permisos de Linux! ¿Realmente es octal?"
[3]: <https://platzi.com/blog/administracion-usuarios-servidores-linux/> "Domina la Administración de Usuarios y Permisos en Servidores Linux"
[4]: <https://www.w3schools.com/python/python_file_handling.asp> "Python file handling"
