# 2D array grid
# Clicking in the grid
# Need to place the mines
# Clicking on the mines
# Placing the numbers
# Right click to flag the mines
# Indicate if you've clicked the mine
# Timer

import pygame
import random

pygame.init()
screen = pygame.display.set_mode([1000, 900])

runGame = True

class Board:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.grid = [['_' for _ in range(10)] for _ in range(8)]
        self.img = pygame.image.load("minesweeper board.png")
    def printBoard(self):
        for row in self.grid:
            print(' '.join(row))
    def generateMines(self, num):
        mines_left = num
        while (mines_left > 0):
            row = random.randint(0, len(self.grid) - 1)
            col = random.randint(0, len(self.grid[0]) - 1)
            if (self.grid[row][col] != "@"):
                self.grid[row][col] = "@"
                mines_left -= 1
            print(mines_left)
    def generateNumbers(self):
        # for each of the squares in the grid:
        #   check if any of the surrounding 8 squares are mine
        #       if they are, add 1 to the number
        # set the value of the square equal to the number of mines around it
        for i in range(8):
            for j in range(10):
                if (self.grid[i][j] == "@"):
                    continue
                num = 0
                if  j + 1 < 10 and(self.grid[i][j+1] == "@"):
                    num += 1
                if j - 1 >= 0 and (self.grid[i][j-1] == "@"):
                    num += 1
                if j + 1 < 10 and i + 1 < 8 and (self.grid[i+1][j+1] == "@"):
                    num += 1
                if i-1 >= 0 and j+1 < 10 and (self.grid[i-1][j+1] == "@"):
                    num += 1
                if i+1 < 8 and j-1 >= 0 and (self.grid[i+1][j-1] == "@"):
                    num += 1
                if i-1 >= 0 and j-1 >= 0 and (self.grid[i-1][j-1] == "@"):
                    num += 1
                if i+1 < 8 and (self.grid[i+1][j] == "@"):
                    num += 1
                if i-1 >= 0 and (self.grid[i-1][j] == "@"):
                    num += 1
                self.grid[i][j] = str(num)
    

gameBoard = Board()
gameBoard.generateMines(10)
gameBoard.generateNumbers()
gameBoard.printBoard()
screen.blit(gameBoard.img, (0, 0))
font = pygame.font.Font("freesansbold.ttf", 32)

def reveal(grid, row, col):
    if (row > 7 or col > 9 or row < 0 or col < 0):
        return 0
    value = grid[row][col]
    if (value == "@"):
        runGame = False
    num = font.render(value, True, "black", "white")
    screen.blit(num, (col * 100 + 50, row * 100 + 50))
    if (value == "0"):
        reveal(grid, row+1, col+1)
        reveal(grid, row, col+1)
        reveal(grid, row-1, col+1)
        reveal(grid, row+1, col-1)
        reveal(grid, row, col-1)
        reveal(grid, row-1, col-1)
        reveal(grid, row+1, col)
        reveal(grid, row-1, col)

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col, row = pygame.mouse.get_pos()
            row = row // 100
            col = col // 100
            reveal(gameBoard.grid, row, col)


    pygame.display.update()

pygame.quit()