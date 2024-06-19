# Paquetes

Un paquete en Python 🐍 es una carpeta que contiene variso modulos. El uso de paquetes es sencillo desde la versión 3.3, si se esta trabajando con una versión anterior debes crear un archivo calve llamado `init.py`

## Ejemplo (Python 3.12.3)

Se tiene una carpeta llamada `pkg`, dentro de ella hay dos módulos:

`mod_1.py`

```python
def func_1():
    return 'func 1'

def func_2():
    return 'func 2'
```

`mod_2.py`

```python
def func_3():
    return 'func 3'

def func_4():
    return 'func 4'
```

Las funciones de cada módulo se pueden importar y usar de la siguiente forma:

```python
# Importando funciones del módulo 1
from pkg.mod_1 import func_1, func_2

# Importando funciones del módulo 2
from pkg.mod_2 import func_3, func_4

print(func_1()) # func 1
print(func_2()) # func 2
print(func_3()) # func 3
print(func_4()) # func 4
```

Podemos importar todo un módulo de un paquete y nombrándolo con la palabara clave `as`

```python
import package.mod_2 as mod_2

print(mod_2.func_3())
print(mod_2.func_4())
```

También podemos usar los paquetes dentro de un módulo que está en el mismo paquete.

`mod_3.py`

```python
from .mod_1 import func_1
from . import mod_2

def func_5():
    return func_1()

def func_6():
    return mod_2.func_3()
```

### Ejemplo (Con archivo `__init__.py`)

Este archivo es obligatorio para versiones anteriores a Python 3.3 ya que sirve para declarar un paquete. Ahora en versiones más nuevas se le agregaron utilidades para inicializar alguna variable o importaciones al paquete.

Siguiendo con el ejemplo dentro de la carpeta `pkg` se crea el archivo `__init__.py`

```python
print("Se inicio paquete")

URL = 'platzi.com'
```

Ahora, cada vez que llame al paquete, automaticamente pasa por `__init__.py`, ejecutando el `print()` e inicializando la vaiable URL. Solo se inicializa la primera vez que lo importamos.

```python
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())

import pkg
print(pkg.URL)
```

**Salida**:

```text
Se inicio paquete
func 1
func 2
func 3
func 4
platzi.com
```

Otro uso para init es crear un `namespace`. Recordando que hay una regla de Python que dice que los espacios de nombre son cosas muy interesantes y hay que hacer más de ellos.

Si intentamos hacer:

```python
import pkg
print(pkg.URL)
print(pkg.mod_1.func_1()) # Error
```

Saldrá un error ya que no tiene la importación explicita `from pkg.mod_1 import func_1`. Por buenas prácticas debería ser posible, para ello se crea un espacio de nombres.

Pueden haber importaciones o funciones que tengan el mismo nombre, esto se soluciona creando `namespaces`.
