# Filter

[◀️](./../README.md)

Es una función que nos sirve para filtrar elementos de una lista. Selecciona ciertos elementos para que pertenezcan a una lista.

Por ejemplo, a la lista [🍔,🍗,🍿,🍟] se le aplica un filtro para obtener los elementos que son vegetarianos y se obtiene [🍿,🍟]. En este caso obtuvimos una lista con dos elementos, peor se puede dar el caso que tengamos una lista con cero elementos.

Algunas otras características son:

- Nunca obtendras una lista con más números que la lista original.
- No modifica la lista original, crea una nueva. No presenta el problema de `map()`

The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.

La función `filter` regresa un iterador resultante de filtrar los elementos de otro iterador a través de una función para ver si son aceptados o no.

## Sintaxis

```python
filter(funcion, iterable)
```

### Parámetros

- **funcion**: Una función que se ejecutará por cada elemento en el iterable.
- **iterable**: Iterable a filtrar.

## Ejemplo

Filtrar los números pares de una lista

```python
numbers = [1,2,3,4,5]

# Da elementos pares dentro de la lista
filter_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filter_numbers) # [2, 4]
```
