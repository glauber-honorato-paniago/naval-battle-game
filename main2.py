import os
import random


def start_game():
    # generating essential game variables and the main table
    positions_divisible_by_5 = []
    positions_divisible_by_5_with_player_marked = []
    player_table = []
    player_life = 30

    for line in range(7):
        for collum in range(7):
            if random.randint(1, 99) % 5 == 0:
                positions_divisible_by_5.append((line, collum))

        player_table.append([' ' for i in range(7)])

    def menu():
        feedback = None
        while True:
            # cleaning the terminal
            # os.system('cls')

            if feedback:
                print(feedback)

            print('\033[93mPara continuar a partida digite [c]\033[0m')
            print('\033[93mPara iniciar um novo jogo digite [n]\033[0m')
            print('\033[93mPara sair do jogo digite [e]\033[0m\n')

            user_input = input('Sua entrada: ').lower()

            # checking user input
            if user_input == 'c':
                return
            elif user_input == 'n':
                return 'BreakGame'
            elif user_input == 'e':
                quit()
            else:
                feedback = 'O valor digitado não é valido!'

    feedback = None
    while True:
        print(positions_divisible_by_5)
        print('Precione [m] para Acessar o Menu.')
        print(f'Jogadas Restantes: {player_life}\n')

        if feedback:
            print(feedback)
            feedback = None

        # printing the column marking lines
        print('  ', end='')
        print(*range(1, 8), sep=' ')

        # printing the direction and player lines
        for line in range(1, 8):
            print(line, sep='\n', end=' ')
            print(*player_table[line - 1])

        # checking gameover
        if player_life < 1:
            print('Fim de jogo: Voce perdeu')
            break

        # main user input
        user_input = input('Sua entrada: ').lower()
        if user_input:
            # checking if player wants to go to menu
            if user_input == 'm':
                return_menu = menu()
                if return_menu == 'BreakGame':
                    start_game()
                    break

            # treating input data and handling its possible errors
            try:
                line, collum = user_input.split(' ')
                line, collum = int(line) - 1, int(collum) - 1
            except:
                feedback = 'Nao foram digitados os valores de linha e coluna corretamente ({numero da linha} {numero da coluna})'
                continue

            # accessing row value and corresponding column
            player_life -= 1

            # game conditions
            player_won = True
            position = (line, collum)
            for value in positions_divisible_by_5:
                if not (value in positions_divisible_by_5_with_player_marked):
                    player_won = False

                print(value, position)
                import time
                print(value == position)
                time.sleep(1)
                if value == position:
                    player_table[line][collum] = 'x'
                    positions_divisible_by_5_with_player_marked.append(position)
                    break
                else:
                    player_table[line][collum] = '0'

            # checking if there is still any number divisible by 5, if there is not the player won
            if player_won:
                print('Voce ganhou!')
                break
            else:
                os.system('cls')


start_game()
