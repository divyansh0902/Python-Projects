from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    #Create a board
    def __init__(self):
        self.board = self.make_board() #we will use a single list to 3x3 board
        self.current_winner = None #keep track of winner

    @staticmethod
    def make_board():
        return [ ' ' for _ in range(9)]

    def print_board(self):
        #this is getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' |')
   
    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 etc tels us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i , spot in enumerate(self.board) if spot == ' '] #list comprehesion
        #moves = []
        #for (i,spot) in enumerate(self.board):
        #    #['x', 'x' ,'0'] --> [(0, 'x'),(1, 'x'),(2, 'o')]
        #    if spot == ' ':
        #        moves.append(i)
        #return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square,letter):
        #if valid move make the move
        #then return true. if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in a row anywhere we have to check all of these
        #first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #but only if square is an even number
        #these are only moves possible to win diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #right to lefy diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all these cgecks fails
        return False

 
def play(game, x_player, o_player, print_game = True):
    #return winner of the game or none for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    #iterate while the game still has empty squares
    # we dont have to worry about winner because we will just retun that which breaks the loop
    while game.empty_squares:
        #get the moves from appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #define a func to make a move
        if game.make_move(square, letter):

            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print('') #empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'  # switches player
            #after we made a move we need to alternate letters
            #if letter == 'X':
            #    letter = 'O'
            #else:
            #    letter = 'X'

        #tiny break
        time.sleep(0.8)


    if print_game:
        print('It\'s a tie!')



if __name__=='__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)