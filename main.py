#Implementation of Two Player Tic-Tac-Toe game in Python.

game_board = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_is_full = False
turn = True
empty = ' '
game = True
# Print the current status of the board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def square_is_taken(board,square_choice):
    if board[square_choice] != ' ':
        print("This Cell is already taken!,please try again ")
        return False
    else:
        return True



def check_horizontal_win(board):
    for i in range(1,8,3):
        if board[f"{i}"] == board[f"{i+1}"] == board[f"{i+2}"]!=empty :
            potential_winner = board[f"{i}"]
            print(f'Game Over {potential_winner} won the game!')
            game = False

def check_vertical_win(board):
    for i in range(1,3):
        if board[f"{i}"] == board[f"{i+3}"] == board[f"{i+6}"]!=empty:
            potential_winner = board[f"{i}"]
            print(f'Game Over {potential_winner} won the game!')
            game = False

def check_diagonal_win(board):
    potential_winner = board["1"]
    if board["1"] == board["5"] == board["9"] !=empty :
        print(f'Game Over {potential_winner} won the game!')

    elif board["3"] == board["5"] == board["7"]!=empty :
        potential_winner = board["3"]
        print(f'Game Over {potential_winner} won the game!')
        game = False

def check_board_status(board):
    check_diagonal_win(board)
    check_horizontal_win(board)
    check_vertical_win(board)

def play(board,turn):
    while board_is_full==False and game:
        square_choice = input()
        if turn ==True:
            print("it's O turn!")
            if square_is_taken(board,square_choice):
                board[square_choice] = 'O'
                turn = False


        else:
            print("it's X turn!")
            if square_is_taken(board,square_choice):
                board[square_choice] = 'X'
                turn = True

        check_board_status(board)
        printBoard(board)
    return


play(game_board,turn)