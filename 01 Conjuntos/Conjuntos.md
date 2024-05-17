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

## Operaciones básicas de consulta

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

## Modificando conjuntos

## Operaciones de conjuntos
