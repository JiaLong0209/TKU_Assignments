import numpy as np
import time


class Table:
    def __init__(self, size=5):
        self.size = int(size)
        self.table = self.createTable(size, size)

    def createTable(self, row, column):
        return np.array([[-1] * column] * row)

    def show(self):
        print('\n{:^40}'.format("Queen's Table"), end='\n\n')
        for n in range(self.size+1):
            if (n):
                print('{:^5}'.format(n), end='')
            else:
                print('{:^10}'.format(''), end='')

        print('{:^5}'.format('(x)'), end='')

        print(end='\n\n\n')

        for i, row in enumerate(self.table):
            print('{:^10}'.format(i+1), end='')
            for j, value in enumerate(row):
                time.sleep(0.005)
                print('{:^5}'.format(self.symbol(value)), end='')
            print(end='\n\n')
        print('{:^10}'.format('(y)'), end='\n\n')

    def symbol(self, n):
        return 'o' if n == 1 else '-'

    def checkLineValid(self, column, row):
        table = self.table
        valid = True
        for i, rowArray in enumerate(table):
            for j, value in enumerate(rowArray):
                # check rows
                if (value == 1 and i == row and j != column):
                    print(f"Error y (row): The position ({j+1},{i+1}) has a queen.")
                    valid = False

                # check columns
                if (value == 1 and j == column and i != row):
                    print(f"Error x (column): The position ({j+1},{i+1}) has a queen.")
                    valid = False

                # check right diagonal  /    i + j = i' + j'
                # The second De Morgan's laws: ¬p∧¬q ≡ ¬(p∨q) 
                # not row == i and not column == j ≡ not(row == i or column == j) 
                if(value == 1 and (row + column == i + j) and not(row == i or column == j)):
                    print(f"Error x or y (right-diagonal): The position ({j+1},{i+1}) has a queen.")
                    valid = False

                # check left diagonal   \    i - i' = j - j'
                if(value == 1 and (row - i == column - j) and not(row == i or column == j)):
                    print(f"Error x or y (left-diagonal): The position ({j+1},{i+1}) has a queen.")
                    valid = False

        return valid

    def isValid(self, column, row):
        # column is x, and row is y
        table = self.table

        # check if the position is outside the table.
        if ((column >= self.size and row >= self.size) or (column < 0 and row < 0)):
            print(f"Error x and y: x {column+1} and y {row+1} is out of the table.")
        elif (column >= self.size or column < 0):
            print(f"Error x: x {column+1} is out of the table.")
        elif (row >= self.size or row < 0):
            print(f"Error y: y {row+1} is out of the table.")
        elif (table[row][column] != -1):
            print("Error x and y: This cell already has a queen.")
        else:
            # check if the entire line is valid
            if (self.checkLineValid(column, row)): return True

        return False

    def put(self, x, y):
        x, y = x-1, y-1
        if (self.isValid(x, y)):
            self.table[y][x] = 1
            return True
        else:
            return False

    def clear(self):
        self.table = self.createTable(self.size, self.size)


class Game():
    def __init__(self):
        self.queens = 0
        self.rounds = 0
        self.table = []
        self.isPlay = False

    def printText(self, str, delta=0.02, end='\n'):
        for i in str:
            time.sleep(delta)
            print(i, end='')
        print(end=end)

    def start(self):
        self.printText("Enter the table size: ", end='')
        self.table = Table(int(input()))
        # self.table = Table()
        self.table.show()
        self.isPlay = True
        while (self.isPlay):
            input_x = input_y = None

            # Check input-x and input-y is a empty string
            while (not input_x):
                self.printText('Enter the x of queen: ', 0.01, end='')
                input_x = input()

            while (not input_y):
                self.printText('Enter the y of queen: ', 0.01, end='')
                input_y = input()

            x = int(input_x)
            y = int(input_y)
            print(type(x), type(y))
            self.isPlay = self.step(x, y)

    def step(self, x=0, y=0):
        if (self.table.put(x, y)):
            self.queens += 1
        else:
            input()
        self.rounds += 1

        self.table.show()
        print('{:^20}'.format(f'Queens: {self.queens}'), end='')
        print('{:^20}'.format(f'Rounds: {self.rounds}'), end='\n\n')

        if (self.queens >= self.table.size):
            return self.restart()

        return True

    def restart(self):

        self.printText("Congratulations! You win the game!!!", 0.04, end='')
        time.sleep(1)

        self.printText("\nYou want to restart the game? (y/n): ", 0.04,  end='')

        answer = input().lower()
        if(answer == 'y'):
            self.printText("Great!",0.05,end='')
            time.sleep(2)
            print('   （๑ • ‿ • ๑ ）')
            time.sleep(1)
            self.reset()
            self.start()
        elif(answer == 'n'):
            self.printText("...\n", 1)
            print('    (╯°Д°)╯ ┻━━┻')
            time.sleep(2)
        else:
            self.printText("...\n\n",1)
            print(' ◢▆▅▄▃ (╯°Д°)╯┻━━━━━━━━━━┻ ▃▄▅▆◣')
            time.sleep(2)

        return False

    def reset(self):
        self.table.clear()
        self.queens = 0
        self.rounds = 0



game = Game()
game.start()
