# Display the grid
# Display X and O
# Placing X and O
# Detecting clicks
# See who wins
# Turns
# Play against computer
# Score for multiple rounds
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]
player = 1 # X is player 1


gridimg = pygame.image.load("week 10/Board.png")
x = pygame.image.load("week 10/X.png")
o = pygame.image.load("week 10/O.png")
def displayGrid():
    screen.blit(gridimg, (0, 0))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                screen.blit(x, (j*200, i*200))
            elif board[i][j] == "O":
                screen.blit(o, (j*200, i*200))
    pygame.display.update()

def place(row, col):
    global player
    if board[row][col] == "_":
        if player == 1:
            board[row][col] = "X"
            player = 2
    if board[row][col] == "_":
        if player == 2:
            board[row][col] = "O"
            player = 1

def checkWin():
    if ((board[0][0] == "X" and board[0][1] == "X" and board[0][2] =="X")or

        (board[1][0] == "X" and board[1][1] == "X" and board[1][2] =="X")or

        (board[2][0] == "X" and board[2][1] == "X" and board[2][2] =="X")or

        (board[0][0] == "X" and board[1][0] == "X" and board[2][0] =="X")or

        (board[0][1] == "X" and board[1][1] == "X" and board[2][1] =="X")or

        (board[0][2] == "X" and board[1][2] == "X" and board[2][2] =="X")or

        (board[0][0] == "X" and board[1][1] == "X" and board[2][2] =="X")or

        (board[2][0] == "X" and board[1][1] == "X" and board[0][2] =="X")):

        return "X wins!"

    if ((board[0][0] == "O" and board[0][1] == "O" and board[0][2] =="O")or

        (board[1][0] == "O" and board[1][1] == "O" and board[1][2] =="O")or

        (board[2][0] == "O" and board[2][1] == "O" and board[2][2] =="O")or

        (board[0][0] == "O" and board[1][0] == "O" and board[2][0] =="O")or

        (board[0][1] == "O" and board[1][1] == "O" and board[2][1] =="O")or

        (board[0][2] == "O" and board[1][2] == "O" and board[2][2] =="O")or

        (board[0][0] == "O" and board[1][1] == "O" and board[2][2] =="O")or

        (board[2][0] == "O" and board[1][1] == "O" and board[0][2] =="O")):

        return "O wins!"
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "_":
                return ""

    return "Tie"
    
    

runGame = True
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col, row = pygame.mouse.get_pos()
            col = col // 200
            row = row // 200
            place(row, col)
            print(checkWin())
            
            
    displayGrid()

pygame.quit()
