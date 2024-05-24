# List Comprehetions

Generas listas con una sintaxis más corta y fácil de leer. Es útil para crear una nueva lista basada en valores de una lista existente.

## Sintaxis

Se usan ls corchetes cuadrados, y se divide en dos partes:

- Un elemento
- Un ciclo de dónde se extraerán elementos de cualquier iterable.

**[** elemento `for` elemento `in` iterable **]**

De tal forma que si queremos hacer una lista con elementos del 1 al 14, con una sola línea podemos hacer lo siguiente:

```python
comprehetion = [element for element in range(1,15)]
```

De esta forma, se comprende que por cada elemento del iterable, vamos a agregar un elemento a la lista.

> 📝 **Nota:** Un **iterable**, es una coleccion (*a.k.a. objeto iterable*) que se recorre haciendo iteraciones, como lo son las listas, las tuplas, los set, etc.

### Agregando condiciones

Se pueden agregar condicionales dentro de la línea que declara una lista con comprehentions, para delimitar si el elemento que vamos a estar trabajando se agrega o no. Este condicional se agrega al final, depués de la parte que representa al ciclo que recorre los elementos del iterable.

**[** elemento `for` elemento `in` iterable `if` condition **]**

De esta forma, por ejemplo, podemos hacer una lista de números del 1 al 100 que son pares, y multiplicarlos por dos.

```python
pares = [i*2 for i in range(1,101) if i % 2 == 0]
```

> 📝 **Nota:** Se puede tomar a la condicion como un filtro que solo acepta elementos que son evaluados como `True`

De esta forma la sintaxis queda algo así

```python
newlist = [expression for item in iterable if condition == True]
```

### La "*expression*"

Es el elemento actual de la iteración, per tambien es la salida, que se puede manipular antes que termine como un elemento de la nueva lista.

```python
newlist = [x.upper() for x in fruits]
```

La *expression* también puede contener condicionales, no como un filtro, si no como otra forma de maniplar la salida. Por ejemplo, meter el item como esta escrito si no es "banana", si es "banana" meter "plátano"

```python
newlist = [x if x != "banana" else "plátano" for x in fruits]
```

![Sintaxis](https://static.platzi.com/media/user_upload/384-a6ba6c3d-656d-40ca-9181-873f654ba5a5.jpg)

## List Comprehention Anidado

Se pueden anidar listas, de forma que tendremos una lista de listas. Se tiene que hacer un for para cada elemento de la sublista.

```python
print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
# [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
```

### Reto

Let's learn about list comprehensions! You are given three integers $x, y$ and $z$ representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by $(i,j,k)$ on a 3D grid where the sum of $i+j+k$ is not equal to $n$. Here, $0 \leq i \leq x; 0 \leq j \leq y; 0 \leq k \leq z$. Please use list comprehensions rather than multiple loops, as a learning exercise.

#### Example

$$
x=1; y=1; z=2; n=3
$$

All permutations of $[i,j,k]$ are:

$$
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
$$

Print an array of the elements that do not sum to $n=3$

$$
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
$$

#### Input format

Four integers $x, y, z$ and $n$, each on a separate line.

#### Constraints

Print the list in lexicographic increasing order.

#### Sample input 0

```text
1
1
1
2
```

#### Sample output 0

```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

#### Explanation 0

Each variable $x, y$ and $z$ will have values of 0 or 1. All permutations of lists in the form $$[i,j,k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]$$
Remove all arrays that sum to $n=2$ to leave only the valid permutations.

#### Sample Input 1

```text
2
2
2
2
```

#### Sample output 2

```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```

> Ve la solución [aqui](./05-1-reto.py) y la fuente [aqui](https://www.hackerrank.com/challenges/list-comprehensions/problem).
