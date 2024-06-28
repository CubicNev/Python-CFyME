# Iterables

[◀️](./../README.md)

En vez de manejar una iteracion de forma automatica con un for, recorriendo de inicio a fin, se puede avanzar en una iteración de forma manual llendo uno por uno de forma secuencial. Esto, por ejemplo, con `range()` se debe convertir en un objeto iterable e ir recorriendolo con la función `next()`.

```python
obj_iter = iter(range(1, 11))

# Iteracion manual:
print(next(obj_iter)) # primer iteracion
print(next(obj_iter)) # segunda iteracion
print(next(obj_iter)) # tercera iteracion
# ...
```

Si se llega de al final de forma manual, y de todas formas seguimos, vamos a generar una excepcion `StopIteration`.

```python
obj_iter = iter(range(1, 4))

print(next(obj_iter)) # primer iteracion
print(next(obj_iter)) # segunda iteracion
print(next(obj_iter)) # tercera iteracion
print(next(obj_iter)) # cuarta iteracion (Error)
```

Salida:

```text
print(next(small_iter))
          ^^^^^^^^^^^^^^^^
StopIteration
```

Se tiene que tener en cuenta hasta que punto se va a iterar o de lo contrario se generar la excepcion. Este error se puede manipular/manejar para que el programa no se detenga.

## Definicion

Un iterador es un `objeto` que contiene un número de valores contables. Este objeto pueder ser **iterado**, lo que quiere decir que puedes moverte a través de todos los valores.

Listas, tuplas, diccionarios y sets son objetos iterables. Son contenedores iterables de los que puedes sacar un *Iterator* usando el método `iter()`

> Fuente: [Python Iterators][1]

<!-- Referencias -->

[1]: <https://www.w3schools.com/python/python_iterators.asp> "Python Iterators"
