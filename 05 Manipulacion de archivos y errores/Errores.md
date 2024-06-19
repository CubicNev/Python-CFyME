# Errores en Python

Python arroja errores bajo ciertas circunstancias, por ejemplo, cuando dividimos entre cero, cuando tenemos un error de sintaxis o el visto anteriormente que se excede el límite de iteración.

> ⚠️ **Cuidado:**  Cada vez que hay un error, el programa termina, se detiene la ejecución. Se deben manejar los errores

## Tipos de errores por defecto

En la siguiente tabla podemos encontrar los errores o excepciones que se presentan en Python.

| Exception | Description |
| --- | --- |
| `AssertionError` | Se genera cuando falla una declaración de afirmación |
| `ArithmeticError` | Se genera cuando se produce un error en los cálculos numéricos |
| `AttributeError` | Se genera cuando falla la asignación o la referencia de atributo |
| `Exception` | Clase base para todas las excepciones |
| `EOFError` | Se genera cuando el método input() alcanza una condición de "fin de archivo" (EOF) |
| `FloatingPointError` | Se genera cuando falla un cálculo de punto flotante |
| `ImportError` | Se genera cuando no existe un módulo importado |
| `GeneratorExit` | Se genera cuando se cierra un generador (con el método close()) |
| `IndentationError` | Se genera cuando la sangría no es correcta |
| `IndexError` | Se genera cuando no existe un índice de una secuencia |
| `KeyError` | Se genera cuando una clave no existe en un diccionario |
| `KeyboardInterrupt` | Se genera cuando el usuario presiona Ctrl+c, Ctrl+z o Eliminar |
| `LookupError` | Se genera cuando no se pueden encontrar los errores generados |
| `MemoryError` | Se genera cuando un programa se queda sin memoria |
| `NameError` | Se genera cuando una variable no existe |
| `NotImplementedError` | Se genera cuando un método abstracto requiere una clase heredada para anular el método |
| `OSError` | Se genera cuando una operación relacionada con el sistema provoca un error |
| `OverflowError` | Se genera cuando el resultado de un cálculo numérico es demasiado grande |
| `ReferenceError` | Se genera cuando no existe un objeto de referencia débil |
| `RuntimeError` | Se genera cuando ocurre un error que no pertenece a ninguna expectativa específica |
| `StopIteration` | Se genera cuando el método next() de un iterador no tiene más valores |
| `SyntaxError` | Se genera cuando se produce un error de sintaxis |
| `TabError` | Se genera cuando la sangría consta de tabulaciones o espacios |
| `SystemError` | Se genera cuando se produce un error del sistema |
| `SystemExit` | Se genera cuando se llama a la función sys.exit() |
| `TypeError` | Se genera cuando se combinan dos tipos diferentes |
| `UnboundLocalError` | Se genera cuando se hace referencia a una variable local antes de la asignación |
| `UnicodeError` | Se genera cuando se produce un problema Unicode |
| `UnicodeEncodeError` | Se genera cuando se produce un problema de codificación Unicode |
| `UnicodeDecodeError` | Se genera cuando se produce un problema de decodificación Unicode |
| `UnicodeTranslateError` | Se genera cuando se produce un problema de traducción Unicode |
| `ValueError` | Se genera cuando hay un valor incorrecto en un tipo de datos especificado |
| `ZeroDivisionError` | Se genera cuando el segundo operador en una división es cero |

> Fuente [Python Built-in Exceptions][1]

## Creando errores propios

Se utiliza el comando `raise` seguido de `Exception(Mensaje)` en donde se lanzara un error con el mensaje ingresado.

```python
# Lanzando excepciones propias
age = 10
# Si la edad es menor a 18 lanza un error (Regla de Negocio)
if age < 18:
    raise Exception('No se permite menores de edad') # Lanzará un error
```

## Manejo de errores

Se evita que se detenga la operacion del programa con el manejo de errores. Usamos `try-except`, que tiene la sintaxis:

```python
try:
    # Bloque de error
except Exception as e:
    # Manejo del error
else:
    # No hubo errores
finally:
    # Pase lo que pase, se ejecuta esto
```

El bloque `try` te permite probar un bloque de código en busqueda de errores.

El bloque `except` te permite ejecutar código cuando ocurre un error (Se puede especificar qué error manejar)

El bloque `else` te permite ejecutar codigo cuando no hay errores.

El bloque `finally` te permite ejecutar codigo sin importar el resultado de los bloques `try-except`

<!-- Referencias -->

[1]: <https://www.w3schools.com/python/python_ref_exceptions.asp> "Python Built-in Exceptions"
