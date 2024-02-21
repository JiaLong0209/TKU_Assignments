import numpy as np
import time

# This code is optimized by ChatGPT 3.5

class Chessboard:
    def __init__(self, size=5):
        self.size = int(size)
        self.board = self.create_board(size, size)

    def create_board(self, rows, columns):
        """
        Create a new chessboard.
        """
        return np.full((rows, columns), -1, dtype=int)

    def display(self):
        """
        Display the chessboard.
        """
        print('\n{:^40}'.format("Queen's Chessboard"), end='\n\n')

        for n in range(self.size + 1):
            if n:
                print('{:^5}'.format(n), end='')
            else:
                print('{:^10}'.format(''), end='')

        print('{:^5}'.format('(x)'), end='\n\n\n')

        for i, row in enumerate(self.board):
            print('{:^10}'.format(i + 1), end='')
            for j, value in enumerate(row):
                time.sleep(0.005)
                print('{:^5}'.format(self.symbol(value)), end='')
            print(end='\n\n')

        print('{:^10}'.format('(y)'), end='\n\n')

    @staticmethod
    def symbol(n):
        """
        Get the symbol for a cell (-1 or 1).
        Returns a string.
        """
        return 'o' if n == 1 else '-'

    def is_valid_position(self, x, y, print_error=True):
        """
        Check if a position is valid in terms of rows, columns, and diagonals.
        x: The x-coordinate (column).
        y: The y-coordinate (row).
        print_error: Whether to print error messages.
        Returns True if the position is valid, False otherwise.
        """
        valid = True

        for i, row_array in enumerate(self.board):
            for j, value in enumerate(row_array):
                if value == 1 and (i == y or j == x or i - j == y - x or i + j == y + x):
                    if print_error:
                        print(f"Error: ({x+1},{y+1}) conflicts with a queen at ({j+1},{i+1}).")
                    valid = False

        return valid

    def place_queen(self, x, y):
        """
        Place a queen on the chessboard.
        x: The x-coordinate (column).
        y: The y-coordinate (row).
        Returns True if the placement is successful, False otherwise.
        """
        if self.is_valid_position(x, y):
            self.board[y][x] = 1
            return True
        else:
            return False

    def clear(self):
        """
        Clear the chessboard.
        """
        self.board = self.create_board(self.size, self.size)


class QueensGame:
    def __init__(self):
        self.queens = 0
        self.rounds = 0
        self.valid_cells = 0
        self.chessboard = None
        self.is_playing = False

    def print_text(self, text, delay=0.02, end='\n'):
        """
        Print text character by character with a delay.
        """
        for char in text:
            time.sleep(delay)
            print(char, end='')
        print(end=end)

    def start(self):
        """
        Start the game.
        """
        self.print_text("Enter the chessboard size: ", end='')
        size = int(input())
        self.chessboard = Chessboard(size)
        self.chessboard.display()
        self.is_playing = True

        while self.is_playing:
            input_x, input_y = None, None

            while input_x is None:
                self.print_text('Enter the x-coordinate for the queen: ', 0.01, end='')
                input_x = input()

            while input_y is None:
                self.print_text('Enter the y-coordinate for the queen: ', 0.01, end='')
                input_y = input()

            x = int(input_x) - 1
            y = int(input_y) - 1
            self.is_playing = self.play_round(x, y)

    def play_round(self, x, y):
        """
        Play a round of the game.
        x: The x-coordinate (column) for placing the queen.
        y: The y-coordinate (row) for placing the queen.
        Returns True if the game continues, False if the game ends.
        """
        if self.chessboard.place_queen(x, y):
            self.queens += 1
        else:
            input()

        self.rounds += 1
        self.chessboard.display()
        self.valid_cells = self.count_valid_cells()
        print('{:^15}'.format(f'Queens: {self.queens}'), end='')
        print('{:^15}'.format(f'Valid Cells: {self.valid_cells}'), end='')
        print('{:^15}'.format(f'Rounds: {self.rounds}'), end='\n\n')

        if self.queens >= self.chessboard.size:
            self.restart_game(is_win=True)
            return False

        if self.valid_cells == 0:
            self.restart_game(is_win=False)
            return False

        return True

    def count_valid_cells(self):
        """
        Count the remaining valid cells on the chessboard.
        Returns the number of valid cells (int).
        """
        valid_cells = 0

        for i in range(self.chessboard.size):
            for j in range(self.chessboard.size):
                if self.chessboard.is_valid_position(j, i, print_error=False) and self.chessboard.board[i][j] != 1:
                    valid_cells += 1

        return valid_cells

    def restart_game(self, is_win):
        """
        Restart the game.
        is_win: Whether the player has won (bool).
        """
        if is_win:
            self.print_text("Congratulations! You win the game!!!", 0.04, end='')
        else:
            self.print_text("What a pity! You lose the game...", 0.04, end='')
        time.sleep(1)

        self.print_text("\nDo you want to restart the game? (y/n): ", 0.04,  end='')
        answer = input().lower()

        while not answer:
            self.print_text("\nDo you want to restart the game? (y/n): ", 0.01,  end='')
            print("(´;ω;`)")
            answer = input().lower()

        self.check_answer(answer)

    def check_answer(self, answer):
        """
        Check the player's answer to restart the game.
        """
        if answer == 'y':
            self.print_text("Great!", 0.05, end='')
            time.sleep(2)
            print('   （๑ • ‿ • ๑ ）')
            time.sleep(1)
            self.reset_game()
            self.start()
        elif answer == 'n':
            self.print_text("...\n", 1)
            print('    (╯°Д°)╯ ┻━━┻')
            time.sleep(2)
        else:
            self.print_text("...\n\n", 1)
            print(' ◢▆▅▄▃ (╯°Д°)╯┻━━━━━━━━━━┻ ▃▄▅▆◣')
            time.sleep(2)

    def reset_game(self):
        """
        Reset the game state.
        """
        self.chessboard.clear()
        self.queens = 0
        self.rounds = 0

# Start the game
if __name__ == "__main__":
    game = QueensGame()
    game.start()
