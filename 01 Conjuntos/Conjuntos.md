# Conjuntos

Un conjunto agrupa elementos que tienen algo en común. Por ejemplo, un conjunto de países.

```text
Paises: {México, Colombia, Bolivia}
```

![Conjunto de países](../Assets/SetPaises.png)

## Propiedades de los conjuntos

- No se puede modificar los valores de los elementos, pero si se puede agregar o eliminar elementos.
- No tienen un orden.
- **No permite duplicados**.

> 📝 **Nota:** El algoritmo de `set` es muy util para extraer elementos de cualquier colección sin repetición. Gracias a que no se pueden repetir elementos.

## Sintaxis

Se usan los corchetes curvos al igual que los diccionarios pero sin usar los pares clave-valor, simplemente se ponen los valores.

```python
set_contries = {'col','mex','bol'}
```

## Tipos de datos dentro de un set

Puede contener cualquier tipo de datos.

```python
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
```

Y tambíen permite tener de varios tipos de datos.

```python
set_types = {1, 'hola', False, 1, 12.12, True}
```

> 📝 **Nota:** `1` y `True` son conciderados como el mismo valor, asi que son tratados como duplicados. Lo mismo pasa con `0` y `False`.

## Operaciones básicas

### Consultar el tipo de dato

Se usa la función `type(dato)`

```python
conjunto = {1, 2, 3 , 4, 5}
print(type(conjunto)) # <class 'set'>
```

### Consultar cuantos elementos contiene

Se usa la función `len(set)`

```python
conjunto = {1, 2, 3 , 4, 5}
print(len(conjunto)) # 5
```

### Crear un set a partir de otra estructura de datos

Se usa el constructor `set()`

```python
conjunto1 = set('Hola') # {'l', 'a', 'H', 'o'}
conjunto2 = set((1, 2, 2, 443, 23)) # {1, 2, 443, 23}
```

### Consultar la existencia de elementos dentro de un set

Se usa el operador `in`.

```python
set_countries = {'col', 'mex', 'bol'}

print('col' in set_countries) # True
print('pe' in set_countries) # False
```

### Recorrer un set con `for`

Se puede recorrer usando `for`como iterador.

```python
for elemento in conjunto:
    print(elemento)
```

## Modificando conjuntos

### Agregando elementos

Se usa el método `add(elemento)`.

```python
conjunto = {'xbox', 'playstation', 'switch', 'pc'}

conjunto.add('celular')
print(conjunto) # {'xbox', 'celular', 'playstation', 'switch', 'pc'}
```

> 📝 **Nota:** No agrega elementos que ya están

### Agregando conjuntos

Se usa el método `update(collection)`.

```python
conjunto1 = {'xbox', 'playstation'}
conjunto2 ={'switch', 'pc'}

conjunto1.update(conjunto2)
print(conjunto1) # {'playstation', 'xbox', 'switch', 'pc'}
```

> 📝 **Nota 1:** Con `update()` también se pueden agregar otras colecciones, como, listas.
> 📝 **Nota 2:** No agrega elementos duplicados.

### Eliminando elementos

Se puede usar `remove(item)` o `discard(item)`. La diferencia entre uno y otro es que el primero lanza un error si el elemento no se encuentra dentro del `set`.

**Ejemplo:** Usando `remove()`

```python
conjunto = {"xbox", "playstation", "switch", "pc"}

conjunto.remove("xbox")
print(conjunto) # {'switch', 'pc', 'playstation'}
conjunto.remove("xbox") # error
```

**Ejemplo:** Usando `discard()`

```python
conjunto = {"xbox", "playstation", "switch", "pc"}

conjunto.discard("xbox")
print(conjunto) # {'pc', 'switch', 'playstation'}
conjunto.discard("xbox")
print(conjunto) # {'pc', 'switch', 'playstation'}
```

> 📝 **Nota:** También es posible usar `pop()`, pero no vas a saber que elemento se va a eliminar porque el set es una coleccion no ordenada.

### Chutate todo el set

Dos formas: `del` elimina el set de la faz de la tierra o `clear()` que solo lo limpa y lo deja sin elementos.

```python
conjunto = {"xbox", "playstation", "switch", "pc"}
print(conjunto) # {'pc', 'playstation', 'xbox', 'switch'}

conjunto.clear()
print(conjunto) # set()
print(len(conjunto)) # 0

del conjunto
print(conjunto) # error
```

## Operaciones de conjuntos

Se siguen las operaciones de conjutos para unir dos o más conjuntos (*sets*). Se tienen:

- Para unir elementos de ambos conjuntos se usa `union()` y `update()`
- `intersection()` mantiene solo los elementos duplicados.
- `difference()` agarra los elementos que estan en el primer conjunto, pero no en el otro (o los demas, si se hace con más de dos conjuntos)
- `symmetric_difference()` agarra todos los elementos, menos los duplicados.

### Union (*join*)

Se usa el método `union(sets)`, da un nuevo conjunto que contiene todos los elementos de todos los conjuntos.

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # {'a', 'c', 1, 2, 'b', 3}
```

Como alternativa se puede hacer lo mismo con el operador `|`.

```python
set3 = set1 | set2
print(set3) # {'a', 'c', 1, 2, 'b', 3}
```

> 📝 **Nota:** Solo funciona para unir sets, no permite otros tipos de colecciones.

Como se mencina anteriormente, se pueden unir varios conjuntos.

```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) # {1, 2, 3, 'bananas', 'cherry', 'John', 'b', 'apple', 'a', 'Elena', 'c'}
myset = set1 | set2 | set3 |set4
print(myset) # {1, 2, 3, 'bananas', 'cherry', 'John', 'b', 'apple', 'a', 'Elena', 'c'}
```

El método `update()`, como fue visto antes, modifica el conjunto original y no da un nuevo conjunto.

### Interseccion (*intersection*)

El método `intersection()` regresa un nuevo conjunto que contiene solo los elementos que tiene en común ambos conjuntos

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # {'apple'}
```

En vez del método se puede usar el operador `&` , pero solo funciona con el tipo de datos `set()`.

```python
set3 = set1 & set2
print(set3) # {'apple'}
```

El método `intersection_update()` hace lo mismo pero en vez de dar un nuevo conjunto modifica el conjunto original.

### Diferencia (*difference*)

Se usa el método `difference()` para crear un conjunto que contenga los elementos que estan en el primer conjunto pero no el segundo.

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3) # {'banana', 'cherry'}
```

Mismo resultado con `-`

```python
set3 = set1 - set2
print(set3) # {'banana', 'cherry'}
```

Y `difference_update()` hace lo mismo alterando el conjunto original.

### Diferencia simetrica (*symmetric_difference*)

`symmetric_difference()` agarra solo los elementos que difieren en ambos conjuntos.

```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) # {'google', 'cherry', 'banana', 'microsoft'}
```

Su operador es `^` y solo funciona operando sets con sets.

```python
set3 = set1 ^ set2
print(set3) # {'google', 'cherry', 'banana', 'microsoft'}
```

`symmetric_difference_update()` para solo modificar el conjunto original
