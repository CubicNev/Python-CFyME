# Módulos

[◀️](./../README.md)

Permiten modularizar una aplciación y encerrar funcionalidades en diferentes archivos. Un módulo en Python 🐍 puede ser un archivo `.py`. Considera que un modulo es similar a una libreria de código.

Python como lenguaje, viene con módulos. Algunos son:

- `random`**:** Funcionalidades de números aleatorios
- `functools`**:** Funciones extra
- `sys`**:** Da información sobre el sistema
- `time`**:** Funcionalidades para manejar hora y fecha
- `collections`**:** Utilidad para manejar listas

## Usar un módulo

Se usa la instruccion `import` seguido del nombre del módulo que se quiere usar.

```python
import modulo
```

### Accediendo a variables y funciones

Para acceder a las variables o funciones del módulo se usa el nombre del módulo seguido de un punto y el nombre de lo que se quiere usar.

```python
# Variable
import sys
print(sys.path)

# Funcion
import time
timestamp = time.time()
```

### Renombrando módulos

Si se desea usar un alias para referirse a algú módulo se hace al momento de importarlo usando la palabra clave `as`.

```python
# Utilidad para manejar listas
import collections as uwu
numbers = [1,1,2,1,2,1,4,5,3,3,21]
# Frecuencia de un número en la lista
counter = uwu.Counter(numbers)
```

### Importar una parte del módulo

Si se desea usar solamente funcionalidades específicas del módulo se puede importar solo esa parte usando la palabra clave `from` seguido del módulo, luego `import` y la  funcionalidad que se desea importar.

Sea el módulo `mymodule.py`

```python
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

> 📝 **Nota:** Un módulo tiene que contenerse en un archivo `.py`

Se importa solo `greeting` de `mymodule`

```python
from mymodule import person1

print(person1["age"])
```

## Creación de módulos propios

Cualquier archivo con extensión `.py` se considera un módulo. Dentro pueden ir funciones, variables y/o clases. Se puede nombrar como queramos siempre y cuando termine en `.py`.

Ejemplo, se crea el archivo `utils.py`

```python
def get_population():
    keys = ['col', 'bol']
    values = [300, 400]

    return keys, values

```

Se importa en el archivo `main.py`

```python
import utils

keys, values = utils.get_population()
print(keys,values)
```

Todo lo que tenga `utils.py` puede ser usado en otros códigos solamente importandolo.

> 📝 **Nota:** Se **modulariza la aplicacion**, y se reutiliza código desde archivos.

## La función dir()

Hay una función integrada por defecto en Python para listar todos las funciones y variables dentro de un módulo.

```python
# Listar todos los nombres definidos al módulo platform
import platform

x = dir(platform)
print(x)
"""
['DEV_NULL', '_UNIXCONFDIR', 'WIN32_CLIENT_RELEASES', 'WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', ...]
"""
```

> Obtenido de [Python Modules][1]

## Módulos como scripts

Los módulos se pueden correr de dos modos:

1. Declarando las funciones del módulo y usandolas al importarlas en otro archivo.
2. Correr el archivo de forma directa como scripts. Pero hay ciertas reglas a seguir, ya que al importar un archivo, este se ejecuta.

Para hacer que al ejecutar un archivo con la dualidad de ser un script pero a la vez un módulo se utiliza `if __name__ == '__main__': run()`.

Este `if` le dice al archivo main.py que si es ejecutado desde terminal, ejecute el método run().

<!-- Referencias -->

[1]: <https://www.w3schools.com/python/python_modules.asp> "Python Modules"
