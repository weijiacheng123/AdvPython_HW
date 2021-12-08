# Please refer to the screenshot of code to understand indentation

# Feel free to ask any doubts by commenting on the answer

# isEmpty(grid, row, column): Checks if the given place in the grid is empty
def isEmpty(grid, row, column):
    if 0<=row<=2 and 0<=column<=2:
        if grid[row][column]=='':
            return 1
        else:
            print('Enter a place with empty cell')
            return 0
    else:
        print('Indexes out of bounds. Enter values between/equal to 0 and 2')
        return 0

# isGridFull(grid): Checks if the grid is full
def isGridFull(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j]=='':
                return 0
    return 1

# printGrid(grid): Prints the grid
def printGrid(grid):
    print(grid[0])
    print(grid[1])
    print(grid[2])

# winner(grid): Tells if anyone has won or not yet
def winner(grid):
    if grid[0][0]=='X' and grid[0][1]=='X' and grid[0][2]=='X':
        return 1
    if grid[1][0]=='X' and grid[1][1]=='X' and grid[1][2]=='X':
        return 1
    if grid[2][0]=='X' and grid[2][1]=='X' and grid[2][2]=='X':
        return 1
    if grid[0][0]=='X' and grid[1][0]=='X' and grid[2][0]=='X':
        return 1
    if grid[0][1]=='X' and grid[1][1]=='X' and grid[2][1]=='X':
        return 1
    if grid[0][2]=='X' and grid[1][2]=='X' and grid[2][2]=='X':
        return 1
    if grid[0][0]=='X' and grid[1][1]=='X' and grid[2][2]=='X':
        return 1
    if grid[0][2]=='X' and grid[1][1]=='X' and grid[2][0]=='X':
        return 1
    if grid[0][0]=='O' and grid[0][1]=='O' and grid[0][2]=='O':
        return 2
    if grid[1][0]=='O' and grid[1][1]=='O' and grid[1][2]=='O':
        return 2
    if grid[2][0]=='O' and grid[2][1]=='O' and grid[2][2]=='O':
        return 2
    if grid[0][0]=='O' and grid[1][0]=='O' and grid[2][0]=='O':
        return 2
    if grid[0][1]=='O' and grid[1][1]=='O' and grid[2][1]=='O':
        return 2
    if grid[0][2]=='O' and grid[1][2]=='O' and grid[2][2]=='O':
        return 2
    if grid[0][0]=='O' and grid[1][1]=='O' and grid[2][2]=='O':
        return 2
    if grid[0][2]=='O' and grid[1][1]=='O' and grid[2][0]=='O':
        return 2
    return 0

# main(): Starts the game
def main():
    grid=[['','',''], ['','',''],['','','']] #Represents the game tic tac toe's board as list of 3 lists containing 3 members each
    gameActive = 1
    while gameActive==1: # Run the game indefinitely in the while loop
# Turn of Player 1 who marks 'X' in the game
        print("\nPlayer 1's turn:")
        printGrid(grid)
        row = int(input("Enter row number {0,1,2}: "))
        column = int(input("Enter column number {0,1,2}: "))
        while isEmpty(grid,row,column)==0:
            row = int(input("Enter row number {0,1,2}: "))
            column = int(input("Enter column number {0,1,2}: "))
        grid[row][column] = 'X'

# Check if the game has finished after Player 1's turn
        result = winner(grid)
        if result==1:
            print('Player 1 wins!')
            break
        if result==0 and isGridFull(grid)==1:
            print('It is a draw.')
            break

# Turn of Player 2 who marks 'O' in the game
        print("\nPlayer 2's turn:")
        printGrid(grid)
        row = int(input("Enter row number {0,1,2}: "))
        column = int(input("Enter column number {0,1,2}: "))
        while isEmpty(grid,row,column)==0:
            row = int(input("Enter row number {0,1,2}: "))
            column = int(input("Enter column number {0,1,2}: "))
        grid[row][column] = 'O'

# Check if the game has finished after Player 1's turn
        print('-----------------------------')
        result = winner(grid)
        if result==2:
            print('Player 2 wins!')
            break
        if result==0 and isGridFull(grid)==1:
            print('It is a draw.')
            break

# Print the game after it has finished
    printGrid(grid)


# Driver code
main()