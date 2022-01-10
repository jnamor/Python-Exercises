## -- TODO --
# Ajouter un mode ordinateur DONE
# Ajouter une identification automatique de victoire/défaite DONE
# Enlever la répétition du code (DRY) DONE
# Vérifier les noms de variables, listes, etc. DONE
# Commenter le code en français DONE
# Traduire DONE

import random

class Board:
    """
    A class to represent a board.

    ...

    Variables:
        LIST_OF_ELEMENT (list): List of all the elements of the game.
        LIST_OF_POSSIBLE_NUMBERS (list): List of all possible combinations (coordinates) of the game.
    """

    LIST_OF_ELEMENT = ['X', 'O']
    LIST_OF_POSSIBLE_NUMBERS = [11, 12, 13, 21, 22, 23, 31, 32, 33]

    def __init__(self):
        """
        Builds an empty list which we will fill over time.
        """
        self.board = []
    
    def create_board(self):
        """
        Fill in the list to create a tic-tac-toe board.  
        
        Args:    
        self (instance): Represents the class instance.
            We can access the attributes and methods of the class in python.  
        """
        for row in range(3):
            self.board.append(["-", "-", '-'])
    
    def players_turn(self, element):
        """
        Introduces the player that it is his turn.  
        
        Args:   
            element (str): The symbol of the current player.    
        """
        print(f"Player {element} turn")
        for i in self.board: print(*i, sep=" ")
    
    def insert_values(self, element):
        """
        Insert the player's symbol in the table. 
        
        Args:    
            element (str): The symbol of the current player.   
            
        Returns:    
            row, line (int): The coordinates of the position.  
            
        Notes:   
            See https://datascientest.com/programmation-orientee-objet-guide-ultime   
            for more info.    
        """
        # asks the player to position his tic-tac-toe
        # the first digit of the number represents the row,
        # the second represents the column
        self.players_turn(element)
        if element == 'X':
            response = [int(i) for i in input("Enter row and column numbers to fix spot: ")]
            while len(response) != 2:
                response = [int(i) for i in input("Please, enter only row and column numbers: ")]
        else:
            response = [int(i) for i in str(random.choice(Board.LIST_OF_POSSIBLE_NUMBERS))]
        row, line = response[0] - 1, response[1] - 1
        
        # asks the player for a new position
        # if it is already taken
        while self.board[row][line] in Board.LIST_OF_ELEMENT:
            print("This location is already taken.")
            row, line = self.insert_values(element)

        # returns the coordinates of the position
        return row, line

    def is_player_winning(self):
        """
        Checks if a player has a current lineup.  
            
        Returns:   
            bool: True    

        Raises:    
            IndexError: Include any IndexError types 
                that the function intentionally raises.     
        """
        global win

        def all_same(items):
            """
            Collects a list.
            If all its arguments are equal, the function returns True.  
        
            Args:    
                items (str): List to analyse.    
                
            Returns:     
                bool: True
            """
            return all(x == items[0] for x in items)

        # collects horizontal, vertical and diagonal alignments
        # by creating a list for each possible composition
        list_horizontal = [[j for j in self.board[i]] for i in range(3)]
        list_vertical = [[j[i] for j in self.board] for i in range(3)]
        list_diagonal = [[list_horizontal[i][i] for i in range(3)], [list_horizontal[::-1][i][i] for i in range(3)]]

        # checks if a single alignment is equal
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
                
        # returns True if this alignment is equal to 'X' or 'O
        if win in Board.LIST_OF_ELEMENT:
            return True

    def play(self):
        """
        Start the game.
        """
        # retrieves the values from the table
        self.create_board()

        # restarts the game as long as a line-up
        # is not spotted on either side
        while self.is_player_winning() != True:
            for element in Board.LIST_OF_ELEMENT:
                row, line = self.insert_values(element)
                self.board[row][line] = element
                
                # cancels the loop if an alignment is found
                if self.is_player_winning() == True:
                    for i in self.board: print(*i, sep=" ")                  
                    break
        
        print(f"\nCongratulations! The player {element} wins")

board = Board()
board.play()