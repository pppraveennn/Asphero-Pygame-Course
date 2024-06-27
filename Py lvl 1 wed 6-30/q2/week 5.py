# Import files
# 2D array for the board
# Placing game pieces
# If a column is available
# Two different game pieces
# Going against the other player (switching turns)
# Detect the win
# Clearing the board
# Sounds

board = [["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"]]

columnIndexTracker = [5, 5, 5, 5, 5, 5, 5]
player = "R"


def checkWin(c):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (j < 4):
                if (board[i][j] == c and board[i][j+1] == c and board[i][j+2] == c and board[i][j+3] == c):
                    return True
            if (i < 3):
                if (board[i][j] == c and board[i+1][j] == c and board[i+2][j] == c and board[i+3][j] == c):
                    return True
            if (j < 4 and i < 3):
                if (board[i][j] == c and board[i+1][j+1] == c and board[i+2][j+2] == c and board[i+3][j+3] == c):
                    return True
            if (j >= 3 and i < 3):
                if (board[i][j] == c and board[i+1][j-1] == c and board[i+2][j-2] == c and board[i+3][j-3] == c):
                    return True
    return False
def printBoard():
    for i in board:
        print(i)

def place(col, player):
    
    row = columnIndexTracker[col]
    board[row][col] = player
    columnIndexTracker[col] -= 1

runGame = True

while runGame:
    printBoard()
    col = int(input("Choose a column: ")) -1
    while (columnIndexTracker[col] < 0):
        print("Invalid!")
        col = int(input("Choose a column: ")) -1
    place(col, player)
    if player == "R":
        player = "Y"
    elif player == "Y":
        player = "R"
    if (checkWin("R")):
        print("Player R wins!")
        runGame = False
    if (checkWin("Y")):
        print("Player Y wins!")
        runGame = False

printBoard()
