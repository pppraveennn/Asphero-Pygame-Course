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
import time

pygame.init()
screen = pygame.display.set_mode([1000, 900])
font = pygame.font.Font("freesansbold.ttf", 50)

runGame = True

class Board:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.grid = [['_' for _ in range(10)] for _ in range(8)]
        self.revealed = [[0 for _ in range(10)] for _ in range(8)]
        self.img = pygame.image.load("minesweeper board.png")
        self.colors = ['black', 'blue', 'green', 'red', 'purple', 'maroon', 'aqua', 'black', 'grey']
    def printBoard(self):
        for row in self.grid:
            print(' '.join(row))
    def displayBoard(self):
        screen.blit(self.img, (0, 0))
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
    def revealMines(self):
        txtImg = font.render("@", True, "red", "white")
        for row in range(8):
            for col in range(10):
                if self.grid[row][col] == "@":
                    screen.blit(txtImg, (col * 100 + 25, row * 100 + 25))
    

    def reveal(self, row, col):
        global runGame
        # convert mouse coordinates to row and column, and check the value
        value = self.grid[row][col]
        if (value == "@"):
            runGame = False
            self.revealMines()
        else:
            txtImg = font.render(value, True, self.colors[int(value)], "white")
            screen.blit(txtImg, (col * 100 + 25, row * 100 + 25))
            self.revealed[row][col] = 1
    
    def checkwin(self):
        count = 0
        for row in range(8):
            for col in range(10):
                if self.revealed[row][col] == 1:
                    count += 1
        return count == 8 * 10 - 10
        

gameBoard = Board()
gameBoard.generateMines(10)
gameBoard.generateNumbers()
gameBoard.printBoard()
gameBoard.displayBoard()


while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # when user clicks, have to find out the value of the square
            # get the mouse coordinates
            col, row = pygame.mouse.get_pos()
            # convert mouse coordinates to row and column
            row = row // 100
            col = col // 100
            gameBoard.reveal(row, col)

            
            # if it is a mine, make it visible
            # if it is a number, show the number
    if gameBoard.checkwin():
        print("win")
    pygame.display.update()

time.sleep(5)
pygame.quit()