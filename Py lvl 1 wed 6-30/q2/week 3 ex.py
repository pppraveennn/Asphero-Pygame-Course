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
         ["R", "_", "_", "_", "_", "_", "_"]]

columnIndexTracker = [4, 5, 5, 5, 5, 5, 5]
player = "R"


def printBoard():
    for i in board:
        print(i)

printBoard()

def place(col, player):
    row = columnIndexTracker[col]
    board[row][col] = "Y"
    columnIndexTracker[col] -= 1
        
