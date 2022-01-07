## -- TODO --
## Ajouter un mode ordinateur
## Ajouter une identification automatique de victoire/défaite
# Enlever la répétition (DRY)
# Commenter le code

import random

class Board:
    def __init__(self):
        self.board = []
    
    def create_board(self):
        for row in range(3):
            self.board.append(["-", "-", '-'])
    
    def insert_values(self, element):                                                           # REPEAT                                       
        print(f"Player {element} turn")
        for i in self.board:
            print(*i, sep=" ")  

        response = [int(i) for i in input("Enter row and column numbers to fix spot: ")]
        while len(response) != 2:
            response = [int(i) for i in input("Please, enter only row and column numbers: ")]

        row = response[0] - 1
        line = response[1] - 1


        return row, line
    
    def insert_values_from_robot(self, element):                                                # REPEAT
        print(f"Player {element} turn")
        for i in self.board:
            print(*i, sep=" ")  

        list_of_possible_numbers = [11, 12, 13, 21, 22, 23, 31, 32, 33]
        response = [int(i) for i in str(random.choice(list_of_possible_numbers))]
        row = response[0] - 1
        line = response[1] - 1

        return row, line

    def is_player_win(self):
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
            
        if win == 'X' or win == 'O':
            return True

    def player(self):
        self.create_board()

        while self.is_player_win() != True:                                                     # REPEAT
            element = 'X'
            row, line = self.insert_values(element)                                             # REPEAT

            while self.board[row][line] == 'O' or self.board[row][line] == 'X':                 # REPEAT
                print("This location is already taken.")                                        # REPEAT

                row, line = self.insert_values(element)                                         # REPEAT

            self.board[row][line] = element                                                     # REPEAT
            
            if self.is_player_win() == True:                                                    # REPEAT
                for i in self.board: print(*i, sep=" ")                                         # REPEAT                   
                break                                                                           # REPEAT

            # ------------------

            element = 'O'
            row, line = self.insert_values_from_robot(element)                                  # REPEAT

            while self.board[row][line] == 'O' or self.board[row][line] == 'X':                 # REPEAT
                print("This location is already taken.")                                        # REPEAT

                row, line = self.insert_values_from_robot(element)                              # REPEAT

            self.board[row][line] = element                                                     # REPEAT

            if self.is_player_win() == True:                                                    # REPEAT
                for i in self.board: print(*i, sep=" ")                                         # REPEAT                   
                break                                                                           # REPEAT
        
        print(f"\nCongratulations! The player {element} wins")    


tableau = Board()
tableau.player()