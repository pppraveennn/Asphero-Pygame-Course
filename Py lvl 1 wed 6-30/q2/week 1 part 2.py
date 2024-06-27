# See who wins
# Play against computer
# Score for multiple rounds
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])

board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]
player = 1 # X is player 1

# at i = 0, j = 0, (0, 0)
# at i = 1, j = 0, (0, 200)
# at i = 1, j = 2, (400, 200)
# at i = 2 j = 1, (200, 400)
# multiply column index by 200 for x value
# multiply row index by 200 for y value


gridimg = pygame.image.load("Board.png")
ximg = pygame.image.load("X.png")
oimg = pygame.image.load("O.png")

def displayGrid():
    screen.blit(gridimg, (0, 0))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                screen.blit(ximg, (j * 200, i * 200))
            elif board[i][j] == "O":
                screen.blit(oimg, (j * 200, i * 200))
                
    pygame.display.update()

def place(row, col):
    global player
    if board[row][col] == "_":
        if player == 1:
            board[row][col] = "X"
            player = 2
        elif player == 2:
            board[row][col] = "O"
            player = 1
    else:
        print("Can't place there!")

def checkWinner():
    for i in range(len(board)):
        if board[i][0] == board[i][1]

runGame = True
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = x // 200
            y = y // 200
            place(y, x)
            
    displayGrid()
        
    
pygame.quit()
