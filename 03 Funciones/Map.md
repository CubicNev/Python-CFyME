# Map

Siguiendo de HOF. Python tiene funciones a las que les podemos mandar funciones (preferiblemente se mandan **lambda functions**).

Map es una función con la que podemos hacer transformación de datos por medio del envío de funciones.

La función principal de Map es hacer transformaciones. Transformaciones a una lista dada de elementos. Las funciones mencionadas iteran sobre las listas.

Por ejemplo, digamos que tenemos una lista de elementos.

[:cow2:, :chicken:, :corn:, :potato:]

Tranformamos cada uno de los elementos, entoces los pasamos por una función, la función `cook()`. Obtenemos como resultado excatamente el mismo array con los elementos transformados

[:hamburger:, :poultry_leg:, :popcorn:, :fries:]

Lo importante es que **tenemos el mismo número de elementos**.

- Tranforma los elementos de una lista.
- Es una HOF, por lo que podemos mandarle funciones.
