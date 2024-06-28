# Reduce

[◀️](./../README.md)

Es de la última funcion de manipulacion de listas que veremos, ya vimos Map y Filter. Trata de reducir algo a un solo valor.

Por ejemplo, con la lista [🍔,🍗,🍿,🍟], esta lista de comida se procesa y se expresa a un solo valor: 💩

Otro ejemplo sería una lisat de números [1,2,3,4], y queremos reducirla a un solo valor:

- Sumando: 10
- Sacando el maximo: 4

> Se saca una conclusión de una lista

La función `reduce(fun,seq)` se usa para aplicar una función en particular a todos los elementos de una lista. Esta definida en el modulo `functools`.

## Sintaxis

```python
# importing functools for reduce()
import functools
functools.reduce(function, iterable)
```

### Parámetros

- **funcion**: Una función que se ejecutará.
- **iterable**: Iterable a reducir.

## Ejemplo

SUmar los elementos de una lista o obtener el elemento mayor.

```python
# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
```

> Obtenido de [reduce() in Python][1]

## Funcionamiento

- Primero, se toman los primeros dos elementos de la secuencia y se obtiene el resultado.
- Luego se aplica la misma funcion al resultado obtenido y al siguiente elemento, guardando ahora este resultado.
- El proceso continua hasta que no quden más elementos en el contenedor.
- El resultado final es retornado.

En la siguiente tabla se explica el procedimiento que se sigue para sumar los elementos de una lista.

| Iteration | Counter | Item | Return |
| :---: | :---: | :---: | :---: |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 2 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 6 | 4 | 10 |

<!-- Referencias -->

[1]: <https://www.geeksforgeeks.org/reduce-in-python/> "reduce() in Python"
