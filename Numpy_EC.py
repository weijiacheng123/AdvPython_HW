def getCoordinates(board):
    while True:
        try:
            row = int(input('Enter row [1-3] :'))
            col = int(input('Enter col [1-3] :'))
            row -= 1
            col -= 1
            if 0 > row or row > 2 or 0 > col or col > 2:
                print('Error: Invalid row/col provided')
            elif board[row][col] == ' ':
                return row, col
            else:
                print('Sorry! That cell is not available')

        except:
            print('Error: Invalid number')


def isWinner(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not ' ':
        return True
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not ' ':
        return True
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] is not ' ':
        return True
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] is not ' ':
        return True
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not ' ':
        return True
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not ' ':
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not ' ':
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] is not ' ':
        return True
    return False


def printBoard(board):
    print('{} | {} | {}'.format(board[0][0], board[0][1], board[0][2]))
    print('-' * 10)
    print('{} | {} | {}'.format(board[1][0], board[1][1], board[1][2]))
    print('-' * 10)
    print('{} | {} | {}'.format(board[2][0], board[2][1], board[2][2]))


def main():

    board = [[' ', ' ', ' '] for row in range(3)]
    valid_moves = 0
    print('Welcome to the game of Tic-Tac-Toe')
    printBoard(board)
    winnerExist = False
    while valid_moves < 9:

        print('Player 1')
        row, col = getCoordinates(board)
        board[row][col] = 'X'
        printBoard(board)
        if isWinner(board):
            print('Player 1 Wins')
            winnerExist = True
            break
        valid_moves += 1
        if valid_moves==9:break
        print('Player 2')
        row, col = getCoordinates(board)
        board[row][col] = 'O'
        printBoard(board)
        if isWinner(board):
            print('Player 2 Wins')
            winnerExist = True
            break
        valid_moves += 1
    if winnerExist is False:
        print('No winners.')


main()