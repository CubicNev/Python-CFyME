# Dictionary Comprehetions

Mismo concepto que [List Comprehentions](List%20Comprehention.md), creación de diccionarios de forma simple y rápida a partir de otras colecciones.

## Sintaxis

```python
{key:value for var in iterable}
```

Al tratarse de diccionarios se usan los *curly brakets* (o llaves) y principalmente se tienen dos partes:

- El par `clave`-`valor`, que es ahora tomado como el elemento de salida o *expression*
- La parte del *terable*, que es el ciclo donde se extraen los elementos de cualquier iterable.

### Condicional

```python
{ key:value for var in iterable if condition}
```

Se agrega una condición al final que sirve de filtro para ver si se agrega o no el elemento al diccionario.

## Función zip()

Hace una union entre una lista y otra.

```python
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages))) # [('nico', 12), ('zule', 56), ('santi', 98)]
```

> 📝 **Nota:** Debe combinarse con el constructor list() para que imprima en forma de lista, si no, solo da una referencia.
