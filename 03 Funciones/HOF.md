# Higher order function (HOF): una función dentro de otra función

Se traduce a "Funciones de Grado Superior". Se refiere a que a una función le enviamos otra función y la ejecutemos desde ahí. Normalmente mandamos variables como atributos de una función, pero también podemos mandar una función como atributo y ejecutarla dentro de la función que la recibe.

## Ejemplo

Se define la función `increment`, que define el paramétro `x` como su entrada. Y de salida retorna `x + 1`

```python
def increment(x):
    return x + 1
```

> 📝 **Nota:** Se modifica el valor de entrada y se da esa modificación como salida

Luego, se crea la función `high_ord_func`, que recibe como parámetros:

- `x`: Un número
- `func`: La **declaración** de una función

```python
def high_ord_func(x, func):
    return x + func(x)
```

De salida da la suma del parámetro `x` más lo que haga la función `func` con `x` como **argumento**.

> ⚠️ **Cuidado:** Recuerda que **parámetro** es cuando se esta definiendo la función y **argumento** es cuando se le pasa un valor a la función.
>
>**Parámetros:** Reglas Internas de la Función.
>
>**Argumentos:** Datos Externos que le Pasamos a la Función para que Pueda Hacer sus Cálculos.

Así, si llamamos a `high_ord_func` usando la definición de `increment` como argumento hariamos la operación $x + (x + 1)$ *i.e.*

```python
result = high_ord_func(2, increment)
print(result) # 2 + (2 + 1)
```

> 📝 **Nota:** No se escribe `increment()` porque si no estariamos ejecutando increment y no se pasaría la función.

## Beneficio

Se agrega modularidad, ya que ahora podemos pasar cualquier función como argumento podemos hacer distintas operaciones sin tener que cambiar la funcion de grado superior.

Juntandolo con `lambdas` tenemos una herramienta muy poderosa.

```python
high_ord_func_lmd = lambda x, func : x + func(x)

result = high_ord_func_lmd(2, lambda x : x + 2)
print(result) # 2 + (2 + 2)
result = high_ord_func_lmd(2, lambda x : x * 5)
print(result) # 2 + (2 * 5)
```

Se agrego moludaridad, y ahora podemos enviar cualquier función que queramos para modificar `x`

## Definición

Una **función de Orden Superior** o en sus siglas **HOF** se le llama así solo cuando contiene otras funciones como parámetro de entrada o devuelve una función como salida, es decir, que en este caso las funciones que operan a otras funciones se les denomina *Higher order function*.

También hay que entender que a estas Funciones de Orden Superior HOF se aplican para funciones y métodos que toman como funciones a los parámetros o devuelven una función como un resultado.

### Propiedades de HOF

- Una función es una instancia de tipo objeto.
- Puede almacenar una función en una variable.
- Puede pasar una función como un parámetro a otra función.
- Puede devolver la función desde una función.
- Se puede almacenar en una estructura de datos como tablas, listas, etc.

#### Funciones como objetos

En Python :snake:, una función puede asinarse a una variable. Esta asignación no llama a la función, en vez de eso, se crea una referencia a la función.

```python
# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()

print(shout('Hello')) # HELLO

# Assigning function to a variable
yell = shout

print(yell('Hello')) # HELLO
```

En el ejemplo, una función es referenciada como el objeto `shout` y crea `yell` como una referencia a el.

#### Pasando una función como un argumento a otra función

Como las funciónes se toman como objetos, pueden ser pasadas como argumentos a otras funciones. Por ejemplo, `greed` toma una funcion como parametro, y se pasa `shout` y `whisper` como argumentos.

```python
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("Hi, I am created by a function \
    passed as an argument.")
    print(greeting)

greet(shout) # HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
greet(whisper) # hi, i am created by a function passed as an argument.
```

#### Retornando una función

Un objeto ser la salida de una función, de esta forma se puede tener una función como una salida.

Por ejemplo, se retona `adder` en `create_adder`

```python
# Python program to illustrate functions
# Functions can return another function
def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(15)
print(add_15(10)) # 25
```

> Más info en [Higher Order Functions in Python][1]

[1]: <https://www.geeksforgeeks.org/higher-order-functions-in-python/> "Higher Order Functions in Python"
