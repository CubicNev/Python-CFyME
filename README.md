# Curso de Python: Comprehensions, Funciones y Manejo de Errores

Curso de Python 🐍 que maneja conceptos como funciones, comprehensions, errores y manejo de archivos. Este repositorio incluye mis notas y prácticas llevadas a traves del curso.

Impartido por: Nicolas Molina
By: Platzi

## Contents

1. [Conjuntos](./01%20Conjuntos/)
    1. [Introduccion a conjuntos](./01%20Conjuntos/Conjuntos.md)
2. [Comprehentions](./02%20Comprehentions/)
    1. [List Comprehentions](./02%20Comprehentions/List%20Comprehention.md)
    2. [Dictionary Comprehentios](./02%20Comprehentions/Dictionary%20Comprehentions.md)
    3. [Comparando colecciones](./02%20Comprehentions/List-Tuple-Set.md)
3. [Funciones](./03%20Funciones/)
    1. [Hablando sobre funciones](./03%20Funciones/Funciones.md)
    2. [Funciones lambda](./03%20Funciones/Lambdas.md)
    3. [Higher Order Function (HOF)](./03%20Funciones/HOF.md)
    4. [Map](./03%20Funciones/Map.md)
    5. [Filter](./03%20Funciones/Filter.md)
    6. [Reduce](./03%20Funciones/Reduce.md)
4. [Módulos](./04%20Modulos/Modulos.md)
    1. [Paquetes](./04%20Modulos/Paquetes.md)

## Brief Introduction

### Zen de Python

Filosofía sobre la que se contruye Python. Se empieza importando `this` (sin albur).

```python
import this # Easter Egg! 🐰🥚
```

Al hacerlo se nos desplegará lo siguiente:

#### The Zen of Python, by Tim Peters

```text
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Si lo traducimos tenemos lo siguiente.

```text
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Espaciado es mejor que denso.
La legibilidad es importante.
Los casos especiales no son lo suficientemente especiales como para romper las reglas.
Sin embargo la practicidad le gana a la pureza.
Los errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
A pesar de que eso no sea obvio al principio a menos que seas Holandés.
Ahora es mejor que nunca.
A pesar de que nunca es muchas veces mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea, ¡tengamos más de esos!
```
