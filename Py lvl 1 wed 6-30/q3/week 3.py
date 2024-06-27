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

while runGame:
    for event in pygame:
        if type == pygame.QUIT:
            runGame = False

pygame.quit()