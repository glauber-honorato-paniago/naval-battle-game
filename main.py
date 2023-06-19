import os
import random

class Game:
    def __init__(self):
        self.reset_game_variables()
    
    def reset_game_variables(self):
        # generating essential game variables and the main table
        self.random_positions_divisible_by_5 = []
        self.player_table = {}
        self.player_life = 30

        list_range = range(1, 8)
        for line in list_range:
            for collum in list_range:
                # gerando numeros varios numeros aleatorios se o mesmo for multiplo de 5 sera adicionado a lista
                if random.randint(1, 99) % 5 == 0:
                    self.random_positions_divisible_by_5.append((line, collum))

                # gerando a tabela de jogadas do jogador (7x7)
                if not line in self.player_table:
                    self.player_table[line] = {}

                self.player_table[line][collum] = ''
  

    def menu(self, type='menu'):
        while True:
            if type != 'victory' and type != 'gameover':
                # cleaning the terminal
                os.system('cls')
                print('Para continuar a partida digite [c]')
            else:
                print('Parabens Voçê venceu!' if type=='victory' else 'Fim de Jogo!')

            print('Para iniciar um novo jogo digite [n]')
            print('Para sair do jogo digite [e]\n')

            user_input = input('Sua entrada: ').lower()

            # checking user input
            if user_input == 'c':
                os.system('cls')
                return
            elif user_input == 'n':
                return self.reset_game_variables()
            elif user_input == 'e':
                quit()

    def user_input_checker(self, user_input):
        # checking if player wants to go to menu
        user_input = user_input.lower()
        if user_input == 'm':
            return self.menu()

        # treating input data and handling its possible errors
        try:
            line, collum = user_input.split(' ')
            line, collum = int(line), int(collum)
        except:
            self.feedback = 'Nao foram digitados os valores de linha e coluna corretamente ({numero da linha} {numero da coluna})'
            return 'continue'

        # accessing row value and corresponding column
        self.player_life -= 1

        if (line, collum) in self.random_positions_divisible_by_5:
            self.player_table[line][collum] = 'x'
            self.random_positions_divisible_by_5.remove((line, collum))

        else:
            self.player_table[line][collum] = '0'

        # checking if there is still any number divisible by 5, if there is not the player won
        if not self.random_positions_divisible_by_5:
            print('Voce ganhou!')
            return 'break'
        else:
            os.system('cls')

    def print_player_table(self):
        print(self.random_positions_divisible_by_5)
        print('Precione [m] para Acessar o Menu.')
        print(f'Jogadas Restantes: {self.player_life}\n')

        if self.feedback:
            print(self.feedback)
            self.feedback = None

        # printing the column marking lines
        print('  ', end='')
        print(*range(1, 8), sep=' ')

        # printing the direction and player lines
        for line in range(1, 8):
            print(line, sep='\n', end=' ')
            print(*self.player_table[line].values(), sep='  ')
   

    def mainloop(self):
        self.feedback = None
        while True:
            self.print_player_table()
            # checking gameover
            if self.player_life < 1:
                print('Fim de jogo: Voce perdeu')
                break

            # main user input
            user_input = input('Sua entrada: ').lower()
            if user_input:
                input_return = self.user_input_checker(user_input)
                if input_return == 'continue':
                    continue

Game().mainloop()
