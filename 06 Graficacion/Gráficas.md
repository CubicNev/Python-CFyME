# Gráficas en Python

Una vez que se extrae información de alguna fuente externa, como un archivo, y además procesar esa información, es útil visualizar los resultados de forma gráfica.

> [Guía definitiva para dominar Matplotlib][1]

## Librería matplotlib

El objetivo de la misma es la visualizacion de datos. Puede generar distintos tipos de gráficas, como *Bar Charts* o *Pie Charts*.

### Instalación

No viene instalado por defecto en Python 🐍. Tenemos que instalarlo para hecerlo parte de nuestro proyecto. Basta con poner el comando:

```shell
pip install matplotlib
```

Desde Git-Bash:

```bash
py -m pip install -U pip py -m pip install -U matplotlib
```

Una vez instalada podemos probar que todo haya salido bien importando la librería.

```python
import pyplot
```

> Pagína de la librería [matplotlib][2]

## Creando gráficas

Para esto se debe importar el módulo `PyPlot`

```python
# Importación con alias
import matplotlib.pyplot as plt
```

### Gráfica de barras

Para comenzar con la creación, se necesitan datos a graficar y la etiquetación de esos datos, por ejemplo:

```python
labels = ['a', 'b', 'c']
values = [100, 200, 80]
```

Se llama a la función `plt.subplots()` la cual regresa una `figura` que representa la gráfica y las coordenadas de origen.

```python
fig, ax = plt.subplots()
```

Damos la instrucción de generar una gráfica de barras tomando como origen el origen obtenido anteriormente `ax`, pasando las etiquetas y los valores que se desean graficar. Y luego se da la instrucción para deplegar la gráfica en la pantalla.

```python
# Grafica datos (gráfica de barras) recibiendo los labels y valores
ax.bar(labels, values)
# Muestra la gráfica
plt.show()
```

### Gráfica de pastel

Se sigue el mismo procedimiento de la Gráfica de barras. Primero tomamos los datos etiquetados que queremos gráficar.

```python
labels = ['a', 'b', 'c']
values = [100, 200, 80]
```

Usamos la función `subplots()` y atrapamos su salida.

```python
fig, ax = plt.subplots()
```

Generamos la gráfica pasando los argumentos necesarios y siguiendo las reglas de la función (Revisar la [libreria][2])

```python
ax.pie(values, labels=labels)
```

Un paso extra, exclusivo de esta gráfica es que se debe dar la instrucción para que se despliegue la gráfica en forma de un círculo. Para que finalmente se depliegue en la pantalla.

```python
ax.axis('equal')
plt.show()
```

> Más info de [Pyplot][3]

<!-- Referencias -->

[1]: <https://platzi.com/blog/matplotlib/> "Platzi Matplotlib"
[2]: <https://matplotlib.org/> "Matplotlib"
[3]: <https://www.w3schools.com/python/matplotlib_pyplot.asp> "Pyplot"
