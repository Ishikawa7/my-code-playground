'''
TIC TAC TOE game
For two player on the same computer
'''
from os import system

players = {'Player1': 'X', 'Player2': 'O'}
board = []
boardSample = ['0', '1', '2', '3', '4', '5', '6', '7', '8']


def reset_board():
    global board
    board = [' '] * 10


def display_board(board):
    system('clear')
    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            print('')
            print('---------------')
        print('| ' + board[i] + ' |', end='')
    print('\n')


def make_move(position, simbol):
    try:
        position = int(position)
        if board[position] == ' ' and position >= 0 and position < 9 and simbol != board[position]:
            board[position] = simbol
            return True
    except BaseException:
        return False


def win_check(board):
    return (
        (
            board[0] == board[1] == board[2] and board[0] != ' ' or
            board[3] == board[4] == board[5] and board[3] != ' ' or
            board[6] == board[7] == board[8] and board[6] != ' ' or
            board[0] == board[3] == board[6] and board[0] != ' ' or
            board[1] == board[4] == board[7] and board[1] != ' ' or
            board[2] == board[5] == board[8] and board[2] != ' ' or
            board[0] == board[4] == board[8] and board[0] != ' ' or
            board[2] == board[4] == board[6] and board[2] != ' '
        )
    )


def game():
    reset_board()
    while True:
        players['Player1'] = input(
            'Player1 chose your simbol (you can use whatever you want): ')
        players['Player2'] = input(
            'Player2 chose your simbol (you can use whatever you want, except for that of player one): ')
        if players['Player1'] == players['Player2']:
            print('Invalid choice of simbols, retry\n')
            continue
        else:
            print('')
            break
    movesCount = 0
    display_board(board)
    while True:
        for player in players.keys():
            while True:
                move = input('{} make move (select position): '.format(player))
                if make_move(move, players[player]):
                    break
                else:
                    print('Invalid move! Retry')
            display_board(board)
            movesCount += 1
            if win_check(board):
                print('{} WIN!!!\n'.format(player))
                return
            if movesCount == 9:
                print("IT'S A DRAW!!!\n")
                return


# GAME MENU
choice = '-'
while choice != 'end':
    print("\nCommands: 'start' to start the game --- 'end' to end the game (Player1 go firstS) ")
    choice = input('Input choice: ')
    if choice == 'end':
        break
    elif choice == 'start':
        display_board(boardSample)
        print('\nThese are the numbers to choose the position of the move\n')
        game()
    else:
        print('Invalid input, retry')
