# 2D array grid
# Clicking in the grid
# Need to place the mines
# Clicking on the mines
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
        pass

gameBoard = Board()
gameBoard.generateMines(10)
gameBoard.printBoard()

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

pygame.quit()