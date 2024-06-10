"""
Proyecto (Refactorizado): Piedra, papel o tijeras
Autor: Carlos Nevárez - CubicNev
Fecha de creación: 7-Jun-2024

Programa que simula el juego piedra, papel o tijera. Usa una modalidad de computadora vs jugador.
Refactorizacion: Se usan funciones
"""
# Importaciones
import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    # Se lee la opción del usuario y se pasa a mnusculas
    user_option = input("piedra, papel o tijera: ").lower()

    # Valida que la opcion ingresada se encuentre dentro de las opciones
    if not user_option in options:
        print('Esa opciones no es valida')
        return None, None
        #continue

    # Se escoge una opcion de forma aleatoria
    computer_option = random.choice(options)

    #Generan opciones para la computadora
    print('User option:', user_option)
    print('Computer option:', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate!")
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print("user gano!")
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('computer gana!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra!')
            print("user gano!")
            user_wins += 1
        else:
            print('tijera gana a papel')
            print("compuer gano!")
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print("user gano!")
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print("compuer gano!")
            computer_wins += 1
    else:
        print("Opcion invalida: ", user_option)

    return user_wins, computer_wins

def who_wins(user_wins, computer_wins):
    if computer_wins == 2:
        print(' COMPUTER WINS!!!!')
        return True
    elif user_wins == 2:
        print(' COMPUTER WINS!!!!')
        return True
    else:
        return False

def run_game():
    # Opciones:
    rounds = 1
    user_wins = 0
    computer_wins = 0

    while True:

        print('*' * 20)
        print('ROUND', rounds)
        print('*' * 20)

        print('computer_wins:', computer_wins)
        print('user_wins:', user_wins)

        user_option, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if who_wins(user_wins,computer_wins): break

        rounds += 1

run_game()