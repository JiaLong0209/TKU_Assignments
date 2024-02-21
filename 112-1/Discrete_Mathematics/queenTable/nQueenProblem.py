import numpy as np
import time


class Table:
    def __init__(self, size=5):
        self.size = int(size)
        self.array = self.createTable(size, size)

    def createTable(self, row, column):
        """
        Create a new table.
        """
        return np.array([[-1] * column] * row)

    def show(self):
        """
        Show the table.
        """
        print('\n{:^40}'.format("Queen's Table"), end='\n\n')
        for n in range(self.size+1):
            if (n):
                print('{:^5}'.format(n), end='')
            else:
                print('{:^10}'.format(''), end='')

        print('{:^5}'.format('(x)'), end='')

        print(end='\n\n\n')

        for i, row in enumerate(self.array):
            print('{:^10}'.format(i+1), end='')
            for j, value in enumerate(row):
                time.sleep(0.001)
                print('{:^5}'.format(self.symbol(value)), end='')
            print(end='\n\n')
        print('{:^10}'.format('(y)'), end='\n\n')

    def symbol(self, n):
        """
        Return the sign of -1 and 1, must be str
        """
        # Queens are represented by the number 1, empty cells by -1.
        return 'Q' if n == 1 else '-'

    def checkLineValid(self, column, row, printError=True):
        """
        Check if this position is valid by the entire lines (rows, columns, and diagonals).
        column: this parameter is the index (x) of the table
        row: this parameter is the index (y) of the table
        printError: whether to print the error messages when checking the position, must be boolean
        return: True if the position is valid, False otherwise
        """
        table = self.array
        valid = True
        for i, rowArray in enumerate(table):
            for j, value in enumerate(rowArray):
                # check rows
                if (value == 1 and i == row and j != column):
                    valid = False

                # check columns
                if (value == 1 and j == column and i != row):
                    valid = False

                # check right diagonal  (/)    i + j = i' + j'
                # The second De Morgan's laws: ¬p∧¬q ≡ ¬(p∨q)
                # not row == i and not column == j ≡ not(row == i or column == j)
                if (value == 1 and (row + column == i + j) and not (row == i or column == j)):
                    valid = False

                # check left diagonal   (\)    i - i' = j - j'
                if (value == 1 and (row - i == column - j) and not (row == i or column == j)):
                    valid = False

        return valid

    def isValid(self, column, row, printError=True):
        """
        Check if this position is valid.
        column: this parameter is the index (x) of the table
        row: this parameter is the index (y) of the table
        printError: whether to print the error messages when checking the position, must be boolean
        return: True if the position is valid, False otherwise
        """
        table = self.array

        if (self.checkLineValid(column, row)):
            return True

        return False

    def place(self, x, y):
        """
        Place the queen on the x and y.
        x: this parameter is the x of the table, not the index
        y: this parameter is the y of the table, not the index
        return: True if this placement is successful, False otherwise
        """
        column, row = x-1, y-1
        if (self.isValid(column, row)):
            self.array[row][column] = 1
            return True
        else:
            return False

    def clear(self):
        """
        Create a new table to clear the table.
        """
        self.array = self.createTable(self.size, self.size)





class Game():
    def __init__(self):
        self.queens = 0
        self.rounds = 0
        self.validCells = 0
        self.table = None
        self.isPlay = False

    def start(self):
        """
        Control the entire game process.
        """
        print("Enter the table size(n): ", end='')
        self.n = int(input())
        self.table = Table(self.n)
        self.isPlay = True
        self.all_cases = self.get_all_permutations(list(range(1,self.n+1)))
        self.remaining = self.get_all_permutations(list(range(1,self.n+1)))
        self.count = 0
        self.valid_count = 0

            
        for this_case in self.remaining: 
            x = 0
            for y in this_case:
                x += 1
                is_valid = self.playRound(x, y)
                if(not is_valid):
                    if(x == self.n): 
                        self.valid_count += 1                 
                        print(f'-'*80)
                        print(f'Case: {this_case}\t Solution Count: {self.valid_count}\t Attemption Count: {self.count}')   
                        self.table.show()

                    self.count += 1
                    self.reset()
                    break;
        print(f"There are {self.count} cases in {self.n} size table with {self.valid_count} solutions. ")


    def playRound(self, x=0, y=0): 
        """ Control the process of a round.
        return: True if the game continues, False otherwise
        """
        # Check whether the position is valid
        if (self.table.place(x, y)):
            self.queens += 1
        else:
            return False

        self.rounds += 1
        self.validCells = self.getValidCells()
        
        # The number of queens on the table >= the size of table implies the player wins.
        if (self.queens >= self.table.size):
            return False

        # The number of valid cells = 0 implies the player loss
        if (self.validCells == 0):
            return False

        return True

    def getValidCells(self):
        """
        Return the remaining valid cells on the table, must be int.
        """
        validCells = 0
        for i in range(self.table.size):
            for j in range(self.table.size):
                if (self.table.isValid(row=i, column=j, printError=False) and (self.table.array[i][j] != 1)):
                    validCells += 1

        return validCells

    def reset(self):
        """
        Reset the value of variables.
        """
        self.table.clear()
        self.queens = 0
        self.rounds = 0

    def get_all_permutations(self, input_list): 
        def permute(p_list = [], index = 0):
            if len(p_list) == len(input_list):         # Condition for ending this function
                total.append(p_list)
                return
    
            for i in range(len(input_list)):             # Call itself using each index of the list
                new_list = [*p_list, input_list[i]]      # Add a new value to the back
                if len(set(new_list)) == len(new_list):  # Check if the list has same value
                    permute(new_list, i)
    
        total = []
        permute()   # Call permute function
        return total



game = Game()
game.start()

