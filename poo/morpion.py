## -- TODO --
# Ajouter un mode ordinateur DONE
# Ajouter une identification automatique de victoire/défaite DONE
# Enlever la répétition DONE
# Vérifier les noms de variables, listes, etc. DONE
# Commenter le code

import random

class Board:
    LIST_OF_ELEMENT = ['X', 'O']
    LIST_OF_POSSIBLE_NUMBERS = [11, 12, 13, 21, 22, 23, 31, 32, 33]

    def __init__(self):
        self.board = []
    
    def create_board(self):
        for row in range(3):
            self.board.append(["-", "-", '-'])
    
    def players_turn(self, element):
        print(f"Player {element} turn")
        for i in self.board: print(*i, sep=" ")
    
    def insert_values(self, element):
        self.players_turn(element)
        if element == 'X':
            response = [int(i) for i in input("Enter row and column numbers to fix spot: ")]
            while len(response) != 2:
                response = [int(i) for i in input("Please, enter only row and column numbers: ")]
        else:
            response = [int(i) for i in str(random.choice(Board.LIST_OF_POSSIBLE_NUMBERS))]

        row, line = response[0] - 1, response[1] - 1
        
        while self.board[row][line] in Board.LIST_OF_ELEMENT:
            print("This location is already taken.")
            row, line = self.insert_values(element)

        return row, line

    def is_player_winning(self):
        global win

        def all_same(items):
            return all(x == items[0] for x in items)

        # checking rows, columns and diagonals
        list_horizontal = [[j for j in self.board[i]] for i in range(3)]
        list_vertical = [[j[i] for j in self.board] for i in range(3)]
        list_diagonal = [[list_horizontal[i][i] for i in range(3)], [list_horizontal[::-1][i][i] for i in range(3)]]

        try:
            win = [i for i in list_horizontal if all_same(i)][0][0]
        except IndexError:
            try:
                win = [i for i in list_vertical if all_same(i)][0][0]
            except IndexError:
                try:
                    win = [i for i in list_diagonal if all_same(i)][0][0]
                except IndexError:
                    pass
            
        if win in Board.LIST_OF_ELEMENT:
            return True

    def play(self):
        self.create_board()

        while self.is_player_winning() != True:
            for element in Board.LIST_OF_ELEMENT:
                row, line = self.insert_values(element)
                self.board[row][line] = element
                    
                if self.is_player_winning() == True:
                    for i in self.board: print(*i, sep=" ")                  
                    break
        
        print(f"\nCongratulations! The player {element} wins")

tableau = Board()
tableau.play()