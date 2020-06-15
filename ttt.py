import os

class Board():
    def __init__(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.num = 0
        self.not_finished = True

    def display_board(self):
        print(' %s | %s | %s ' %(self.cells[0], self.cells[1], self.cells[2]))
        print('-----------')
        print(' %s | %s | %s ' %(self.cells[3], self.cells[4], self.cells[5]))
        print('-----------')
        print(' %s | %s | %s ' %(self.cells[6], self.cells[7], self.cells[8]))

    def refresh(self):
        os.system('clear')
        board.display_board()

    def add(self, n, strr):
        if n.isnumeric():
            if int(n) > 0 and int(n) < 10:
                if self.cells[int(n)-1] == ' ':
                    self.cells[int(n)-1] = strr
                    self.num += 1

    def check_winner(self):
        if self.cells[0] == self.cells[1] == self.cells[2] == 'X' or self.cells[3] == self.cells[4] == self.cells[5] == 'X' or self.cells[6] == self.cells[7] == self.cells[8] == 'X'\
        or self.cells[0] == self.cells[3] == self.cells[6] == 'X' or self.cells[1] == self.cells[4] == self.cells[7] == 'X' or self.cells[2] == self.cells[5] == self.cells[8] == 'X'\
        or self.cells[0] == self.cells[4] == self.cells[8] == 'X' or self.cells[2] == self.cells[4] == self.cells[6] == 'X':
            self.not_finished = False
            print('X player won')
            self.play_again()
        if self.cells[0] == self.cells[1] == self.cells[2] == 'O' or self.cells[3] == self.cells[4] == self.cells[5] == 'O' or self.cells[6] == self.cells[7] == self.cells[8] == 'O'\
        or self.cells[0] == self.cells[3] == self.cells[6] == 'O' or self.cells[1] == self.cells[4] == self.cells[7] == 'O' or self.cells[2] == self.cells[5] == self.cells[8] == 'O'\
        or self.cells[0] == self.cells[4] == self.cells[8] == 'O' or self.cells[2] == self.cells[4] == self.cells[6] == 'O':
            self.not_finished = False
            print('O player won')
            self.play_again()

    def start_game(self):
        bool = True
        move  = 'X'
        while self.not_finished:
            self.refresh()
            self.check_winner()
            nu = input("Please enter the position(1-9):")
            self.add(nu,move)
            if bool:
                move = 'O'
                bool = False
            else:
                move = 'X'
                bool = True
            self.refresh()
            if self.num == 9:
                self.not_finished = False

    def reset_board(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.num = 0
        self.not_finished = True
        os.system('clear')
        self.display_board()

    def play_again(self):
        again = input("Would you like to play again? (Y / N)  ")
        if again == 'Y' or again == 'y':
            self.reset_board()
        else:
            exit()

board = Board()
board.start_game()
