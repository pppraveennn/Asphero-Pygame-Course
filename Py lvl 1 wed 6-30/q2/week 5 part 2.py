import pygame

pygame.init()
screen = pygame.display.set_mode([700, 600])

runGame = True

boardImg = pygame.image.load("connect 4 board.png")
yellow = pygame.image.load("yellow.png")
red = pygame.image.load("red.png")

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
    screen.blit(boardImg, (0, 0))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                screen.blit(red, (j*100+5, i*100+5))
            elif board[i][j] == "Y":
                screen.blit(yellow, (j*100+5, i*100+5))
    
def place(col, player):
    
    row = columnIndexTracker[col]
    board[row][col] = player
    columnIndexTracker[col] -= 1


while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col, row = pygame.mouse.get_pos()
            col = col // 100
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

    pygame.display.update()

pygame.quit()
