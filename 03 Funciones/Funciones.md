# Funciones

Una función es un bloque de código que se ejecuta cuando se llama, se pueden hacer llamadas a funciones multiples veces y en muchos puntos. Contiene un espacio al que le pueden pasar datos de entrada, conocidos como **parámetros**, y puede regresar datos de salida, resultado de las operaciones hechas dentro de la función.

Con la funciones se cumple **el principio DRY** (*Don't Repeat Yourself), que consiste en no repetir un bloque de código con la misma lógica una y otra vez, al tener funciónes que nos ahorrran el estar escribiendo las mismas instrucciones una y otra vez, tenemos un código más limpio y escalable.

> 📝 **Nota:** Previamente ya hemos trabajado con funciones, por ejemplo, la función `print(mensaje)` que imprime en la terminal lo que le pasemos como argumentos cuando la llamamos.

## Sintaxis

Se usa la palabra clave `def` seguida del nombre de la función y unos parentesís donde pueden ir o no argumentos de entrada para la función, y dos puntos `:`.

```python
def funcion(a, b):
    c = a + b
    return c
```

Se usa la identación para definir el bloque de código que conforma a la función.

Una función puede dar datos de salida, usando la palabra calve `return`

## Llamar a una función

Para llamar a unsa función solo se debe poner el nombre de la función seguido de parentesís.

```python
def saluda():
    print("Saludos desde la función")

saluda()
```

> 📝 **Nota:** Si una función tiene parametros de entrada, estos se deben brindar al momento de hacer la llamada a función. "Se le deben pasar argumetos".
