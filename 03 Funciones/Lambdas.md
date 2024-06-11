# Funciones anónimas: lambda λ

Son funciones especiales que brindan una gran versatilidad a la hora de declarar funciones. Se maneja cierta sintaxís para estás funciones.

Una fución tradicional tiene una entrada y una salida, por ejemplo:

```python
def incrementa(x):
    return x + 1
```

La función `incrementa()` recibe un número `x` de entrada y de salida da el número aumentado en 1 (`x + 1`). Está función se puede representar como una **lambda function**.

```python
lambda x : x + 1
```

Pueden tener varios argumentos

```python
lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'
```

## Sintaxis

De esta forma, podemos definir a una función lambda como una pequeña función anonima, que puede tomar cualquier número de argumentos pero solo puede tener una expresión para la salida. *i.e.*

> `lambda` *argumentos* `:` *expresión*

Consiste en la palabra clave `lambda` seguido de los argumentos de la función, poniendo `:` y continuando con la expresión que dará la salida.

Se puede asignar una función a una variable.

```python
incrementa = lambda x : x + 1
```

## ¿Por qué usar lambdas?

Sirven para darle modularidad a las función, esto es posible usando la versión de función anonima (sin asignarse a una variable) dentro de una función.

**Por ejemplo**: Una función que tome un argumento, y que ese argumento sea multiplicado por un número desconocido.

```python
def multiplcador(n):
  return lambda a : a * n
```

De esta forma podemos tener fuciones que siempre dupliquen o tripliquen un número.

```python
def multiplcador(n):
  return lambda a : a * n

duplicar = multiplcador(2)
triplicar = multiplcador(3)

print(mydoubler(11))
print(mytripler(11))
```
