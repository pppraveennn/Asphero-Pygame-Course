""" Data Structure"""
# 9x9 board
# 3x3 grids within the 9x9

"""Board Generation"""
# certain numbers need to be displayed (starting configuration)
# has to be solvable each time

"""Check for Correctness"""
# each 3x3 grid has to have only 1 of each number
# each row/col has to have only 1 of each number
# if the number is wrong, make it red
# 3 strikes rule

"""User Input"""
# numbers 1-9
# highlight the square you are editing
# click to type in a number
# make sure you cant type where there is already a number

import pygame

pygame.init()
screen = pygame.display.set_mode([900, 900])
font = pygame.font.Font("freesansbold.ttf", 50)

runGame = True

class Board:
    def __init__(self):
        self.img = pygame.image.load("sodoku board.png")
        self.grid = self.grid = [['_' for _ in range(9)] for _ in range(9)]
    def displayBoard(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != '_':
                    txt = font.render(self.grid[i][j], True, "black", "white")
                    screen.blit(txt, (j * 100 + 50-txt.get_rect().width/2, i * 100 + 50-txt.get_rect().width/2))

board = Board()

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            col, row = pygame.mouse.get_pos()
            row = row // 100
            col = col // 100
            if event.key == pygame.K_1:
                board.grid[row][col] = "1"
            if event.key == pygame.K_2:
                board.grid[row][col] = "2"
            if event.key == pygame.K_3:
                board.grid[row][col] = "3"
            if event.key == pygame.K_4:
                board.grid[row][col] = "4"
            if event.key == pygame.K_5:
                board.grid[row][col] = "5"
            if event.key == pygame.K_6:
                board.grid[row][col] = "6"
            if event.key == pygame.K_7:
                board.grid[row][col] = "7"
            if event.key == pygame.K_8:
                board.grid[row][col] = "8"
            if event.key == pygame.K_9:
                board.grid[row][col] = "9"
            if event.key == pygame.K_SPACE:
                board.grid[row][col] == '_'


    screen.fill((255, 255, 255))
    screen.blit(board.img, (0, 0))
    board.displayBoard()
    pygame.display.update()


pygame.quit()