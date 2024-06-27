# Proyecto final del curso: Gráficar la población de un país

A partir de la información de `[data.csv](./data.csv)`. Gráficar la información de un país.

- Seleccionar solo la información poblacional, ignorando todo lo demás.
- Permitir ver el crecimiento poblacional del país a traves de los años con un **Bar Chart**

## Puntos clave

- Los datos del CCV se extraen y se pasan a un formato de diccionario, en el módulo [read_csv.py](./read_csv.py).

```python
{
    'Rank': 28,
    'CCA3': 'COL' ,
    'Country': 'Colombia' ,
    'Capital': 'Bogota',
    'Continent': 'South America'
    '2022 Population': 3000,
    '2020 Population': 400,
    '2015 Population': 500,
    'World Population Percentage': 0.12
}
```

---

- Para hacer una gráfica del crecimiento poblacional a través de los años se debe obtener solo los años con su valor correspondiente como entero.

```python
{
    '2022': 3000,
    '2020': 400,
    '2015': 500,
    '2010': 12,
    '2000': 12,
    '1990': 23,
    '1980': 12,
    '1970': 12
}
```

Una solucion es hacer una función que extraiga unicamente los datos de crecimiento poblacional y les de el formato deseado.

```python
def extract_anual_population(data):
    datos_poblacionales = []
    # recorre los datos de cada país
    for country in data:
        # Hace un diccionario tomando unicamente los datos de poblacion anual
        # Formatea para solo tomar el año y pasa la poblacion a entero
        population = {year[0:4]:int(amount) for (year, amount) in country.items() if str(year).endswith('Population')}
        datos_poblacionales.append(population)
    return datos_poblacionales
```

> 📝 **Nota:** Esta funcion se implemento en [read_csv.py](utils.py)

Otra solución es recibiendo unicamente la información de un país, y a partir de ese extraer unicamento los datos de crecimiento poblacional de forma "manual".

```python
def get_population(country_dict):
    # Seleccion manual
    population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values
```

> 📝 **Nota:** Esta adición se hizo en [utils.py](./utils.py)

La primera opcion reacondicionada a funcionar como la segunda opcion.

```python
def get_anual_population(country_dict):
    return {year[0:4]:int(amount) for (year, amount) in country_dict.items() if str(year).endswith('Population')}
```
