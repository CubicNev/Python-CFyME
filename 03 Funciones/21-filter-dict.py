"""
Filtros con diccionarios
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Tue 18-Jun-2024

Se utiliza la función filter() con un diccionario sin que se modifique el estado original
"""
matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]
print(matches)
print(len(matches)) # Tiene 3 elementos

# Filtra las partidas ganadas
lista_filtrada = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(lista_filtrada)
print(len(lista_filtrada)) # Tiene 2 elementos
