# Map

Siguiendo de HOF. Python tiene funciones a las que les podemos mandar funciones (preferiblemente se mandan **lambda functions**).

Map es una función con la que podemos hacer transformación de datos por medio del envío de funciones.

La función principal de Map es hacer transformaciones. Transformaciones a una lista dada de elementos. Las funciones mencionadas iteran sobre las listas.

Por ejemplo, digamos que tenemos una lista de elementos: [🐄, 🐓, 🌽, 🥔]

Tranformamos cada uno de los elementos, entoces los pasamos por una función, la función `cook()`. Obtenemos como resultado excatamente el mismo array con los elementos transformados: [🍔, 🍗, 🍿, 🍟]

Lo importante es que **tenemos el mismo número de elementos**.

- Tranforma los elementos de una lista.
- Es una HOF, por lo que podemos mandarle funciones.

La función `map()` ejecuta una funcion por cada elemento de un iteravle. Tl elemento es mandado a la función como argumento.

## Sintaxis

```python
map(function, iterables)
# Alternativa
map(function, iterable[, iterable1, iterable2,..., iterableN])
```

### Parámetros

- **funcion**: La función que se va a ejecutar sobre cada elemento.
- **iterable**: Un objeto de coleccion, secuencia o iterable. Puedes mandar tantos iterables como quieras, solo tienes que asegurarte que la función tiene un parámetro para cada itereble.

## Ejemplos

Calcular la longitud de cada palabra en un tupla.

```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

# Con lambda:
x = map(lambda x: len(x), ('apple', 'banana', 'cherry'))
```

Sumar los elementos de dos listas

```python
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
```

> 📝 **Nota:** En el ejemplo anterior se toma como base la lista más pequeña, es decir, el resultado tendrá tres elementos.

## Map con diccionarios

Se pueden hacer transformaciones no tan convecionales. Siguiendo el ejemplo anterior donde tenemos la lista de comida [🍔,🍗,🍿,🍟]. Podríamos hacer una transformación en la que ahora se tengan vehiculos [🚓,🚎,🚙,🛺].

En este caso, podemos transformar los tipos de datos. De diccionarios a números.

### Ejemplo

Se tiene una lista de diccionarios que contienen infromación sobre productos. Se quiere obtener una lista de precios.

```python
# Lista de diccionarios
items = [
    {
        'producto': 'camisa',
        'price': 100
    },
    {
        'producto': 'pantalones',
        'price': 300
    },
    {
        'producto': 'shorts',
        'price': 200
    }
]

# Quiero una lista con precios
prices = list(map(lambda item: item['price'], items))
print(prices)
```

Ahora se desea agregar un atributo al diccionario que contenga los impuestos.

```python
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

items_w_taxes = list(map(add_taxes, items))

print(items_w_taxes)
```

> 📝 **Nota:**  `map()` no modifica, crea uno nuevo. Pero en este caso de agragar un elemento al diccionario sí cambio la lista original. Este problema es debido a una **referencia a memoria**.

Tienes que tener cuidado al trabajar con diccionarios. Ya que al modificar un atributo de un diccionario puede que estés modificando toda la coleccion original y no creando una nueva. Si no es un comprtamiento esperado puede causar problemas.

### Reto: Map con inmutabilidad

Al modificar un atributo de un diccionario no debería modificarse la colección original. Este problema ocurre por la referencia en memoria, en la computadora hay un espacio que contiene al diccionario, en vez de trabajar con un nuevo valor (como cualquier operación que cre un espacio para el resultado) se trabaja con la referencia en memoria lo que hace que las modificaciones se hagan directamente en el original.

Este problema esta en

```python
def add_taxes(item):
    item['taxes'] = item['price'] * .19 # Aqui
    return item
```

El elemento que se esta agregando `item['taxes']` tiene la referencia en memoria que apunta al diccionario original. Normalmente se crea un nuevo elemento que copia el elemento del diccionario original. Lo que hace que se copie sin traer la referencia.

```python
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19 # Aqui
    return item
```

Esto tiene que ver con los conceptos de **mutabilidad e inmutabilidad**.

### Otras alternativas

#### 1

```python
items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

new_items = list(map( lambda x: x|{'tax': x['price']*0.19} ,items))

print(new_items)
print(items)
```

```json
[{'product': 'shirt', 'price': 120, 'tax': 22.8}, {'product': 'pants', 'price': 160, 'tax': 30.4}, {'product': 'socks', 'price': 205, 'tax': 38.95}]

[{'product': 'shirt', 'price': 120}, {'product': 'pants', 'price': 160}, {'product': 'socks', 'price': 205}]
```

#### 2

```python
tax = .19
new_items = list(map(
    lambda item: {**item, **{'tax':item['price']*tax}}, items
    ))
print(new_items)
```

```json
[{'product': 'shirt', 'price': 120, 'tax': 22.8}, {'product': 'pants', 'price': 160, 'tax': 30.4}, {'product': 'jacket', 'price': 205, 'tax': 38.95}]
```

#### 3

Este es mi aporte teniendo en cuenta algunas soluciones que plantearon otros compañeros, hago uso del ** para desempaquetar el diccionario, recomiendo leer más acerca de esta característica puesto que su uso es variado:

```python
items = [
  {
    'product': 'tshirt',
    'price': 100,
  },
  {
    'product': 'pants',
    'price': 300,
  },
  {
    'product': 'blue white pants',
    'price': 200,
  },
]

newItems = map(lambda item: {**item, 'tax': item['price'] * .19}, items)

print(list(newItems))
```

> Ir a [Asterisco * y Doble Asterisco ** en Python: Qué Son y Cómo Usarlos](https://www.codigopiton.com/como-usar-asterisco-y-doble-asterisco-en-python/)
