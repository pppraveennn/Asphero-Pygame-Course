player = "R"

board = [["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_", "_", "_"]]

def printBoard():
    for i in board:
        print(i)

printBoard()

def place(col, player):
    global board
    for i in range(5, 0, -1):
        print(i)
        print(col)
        if board[i][col] == "_":
            board[i][col] = player
            break

place(0, player)
player = "Y"
place(0,  player)
printBoard()
        
