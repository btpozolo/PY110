
import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
PLAYER = ['User', 'Computer']
winner = ''

def display_board(board):
    os.system('clear')
    print('-----------------')
    print('|  Tic-Tac-Toe  |')
    print('-----------------')
    prompt(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
    print('')
    print('     |     |')
    print(f'  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}')
    print('     |     |')
    print('')

def initialize_board():
    return([[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']])

def prompt(message):
    print(f'==> {message}')

def get_col(number):
    num = (number - 1) % 3
    return num

def get_row(number):
    num = (number - 1) // 3
    return num

def player_chooses_square(board):
    
    while True:
        valid_moves = get_valid_moves(board)
        prompt(f'Please select a square: {valid_moves}')
        square = input()
        try:
            square = int(square)
            if square in valid_moves:
                break
        except ValueError:
            display_board(board)
            prompt('Please enter a number.')
            continue
        display_board(board)
        prompt('Sorry, that\'s not a valid choice')
    
    mark_move(square, PLAYER[0], board)

def computer_chooses_square(board):
    valid_moves = get_valid_moves(board)
    if not valid_moves:
        return
    square = random.choice(valid_moves)
    mark_move(square, PLAYER[1], board)

def get_valid_moves(board):
    flatten_board = [square == INITIAL_MARKER for row in board
                                    for square in row]
    return ([index + 1 for index, square in enumerate(flatten_board) if square])

def mark_move(square, player, board):
    row = get_row(square)
    col = get_col(square)
    board[row][col] = COMPUTER_MARKER if player == PLAYER[1] else HUMAN_MARKER

def board_full(board):
    return False if get_valid_moves(board) else True

def detect_winner(board):
    # Check rows 
    for row in range(3):
        first_mark = board[row][0]

        if first_mark == INITIAL_MARKER:
            continue

        if all(board[row][col] == first_mark for col in range(1, 3)):
            return PLAYER[0] if first_mark == HUMAN_MARKER else PLAYER[1]

    # Check cols
    for col in range(3):
        first_mark = board[0][col]

        if first_mark == INITIAL_MARKER:
            continue

        if all(board[row][col] == first_mark for row in range(1, 3)):
            return PLAYER[0] if first_mark == HUMAN_MARKER else PLAYER[1]

    # Check diags
    if board[1][1] != INITIAL_MARKER:
        first_mark = board[1][1]
        if board[0][0] == first_mark and board[2][2] == first_mark:
            return PLAYER[0] if first_mark == HUMAN_MARKER else PLAYER[1]
        if board[2][0] == first_mark and board[0][2] == first_mark:
            return PLAYER[0] if first_mark == HUMAN_MARKER else PLAYER[1]

    return False

def someone_won(board):
    return bool(detect_winner(board))

def play_tic_tac_toe():
    while True:
        board = initialize_board()

        while True:
            display_board(board)

            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

        display_board(board)
        if someone_won(board):
            prompt(f'{detect_winner(board)} won!')
        else:
            prompt("It's a tie!")
        
        prompt('Play again? (y/n)')
        if input().strip().lower()[0] != 'y':
            break
    prompt('Thanks for playing!')

play_tic_tac_toe()