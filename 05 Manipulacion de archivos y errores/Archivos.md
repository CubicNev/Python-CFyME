# Manipulación de archivos

Python permite la lectura y escritura de distintos archivos (por ejemplo los `.txt`)

## Abrir un archivo

Hay dos formas. La primera consiste en usar la función `open(file)` para almacenar el archivo en una variable y tabajar sobre el usando esa variable, en este caso es recomendable usar la función `close()` cuando se termine de trabajar en el archivo para no usar tantos recursos.

```python
# Abrimos el archivo
file = open("./text.txt")
# Cuando se termina de trabajar con el archivo, debe cerrarse para no gastar recursos
file.close()
```

La segunda forma se hace con el comando `with`, permitiendo que se ejecute un bloque de codigo para manipular el archivo y una vez termine, este se cierre de forma automatica sin tener que usar `close()`

```python
with open('./text.txt') as file:
    # Leer archivo linea a linea
    for line in file:
        print(line)
```

> ⚠️ **Cuidado:** Al usar `open()` por defecto solo viene con permisos de lectura.

La función `open()` toma dos parámetros: `filename` y `mode` Existiendo cuatro formas de abrir un archivo.

1. `r` (**read**). Es el valor por defecto. Abre el archivo para leerlo, manda error si el archivo no existe.
2. `a` (**append**). Abre el archivo para agregarle contenido, crea el archivo si no existe.
3. `w` (**write**). Abre el archivo para escribir, crea el archivo si no existe.
4. `x` (**create**) Crea el archivo especificado, regresa un error si el archivo no existe.

Adicionalmente puedes específicar si el archivo debe manejare como un binario o como texto plano:

- `t` (**text**). Modo por defecto, abre en modo de texto plano.
- `b` (**binary**). Abre en modo binario (ej. imagenes)

Cuando se abre un archivo, sin especificar un modo, por default se ejecutaría asi

```python
f = open("demofile.txt", "rt") # Abre como texto plano en modo lectura
```

> Más información sobre los permisos: [Permisos en linux][2], [Administración de usuarios][3]. Fuente [aqui][4].

## Leer un archivo

Hay varias funciones: `read()` lee todo el archivo de una sola vez, `readline()` lee una línea a la vez funcionando como un iterador, también podemos leerlo recorriendolo con un `for` a manera de iterable.

```python
# Leer todo el archivo
print(file.read())

# Lectura linea a linea (como iterador)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# Lectura linea a linea con un for (iterable)
for line in file:
    print(line)
```

## Modificar un archivo

Para escribir se usa `open()` con los parametros `a` (*append*, agrega contenido al final del archivo, también hce lo mismo `r+`) o `w` (*write*, va a **sobreecribir** el contenido existente).

```python
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# r+ para permisos tanto de lectura como de escritura. Enfocado en agregar
# nuevo contenido al contenido existente en el archivo
# w+ para permisos tanto de lectura como de escritura. Enfocado en reescribir
# el contenido existente
```

> Más info sobre manejo de archivos [aqui][1]

<!-- Referencias -->

[1]: <https://realpython.com/working-with-files-in-python/> "Working With Files in Python"
[2]: <https://platzi.com/blog/cosas-que-nos-sabias-sobre-el-sistema-de-permisos-de-linux-realmente-es-octal/> "¡Cosas que nos sabías sobre el sistema de permisos de Linux! ¿Realmente es octal?"
[3]: <https://platzi.com/blog/administracion-usuarios-servidores-linux/> "Domina la Administración de Usuarios y Permisos en Servidores Linux"
[4]: <https://www.w3schools.com/python/python_file_handling.asp> "Python file handling"
