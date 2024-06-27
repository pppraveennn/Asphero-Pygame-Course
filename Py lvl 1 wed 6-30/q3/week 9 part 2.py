import pygame
import startingboards

pygame.init()
screen = pygame.display.set_mode([900, 900])
font = pygame.font.Font("freesansbold.ttf", 50)

runGame = True

class Board:
    def __init__(self):
        self.starting_boards = startingboards.StartingBoards()
        self.img = pygame.image.load("sodoku board.png")
        self.grid = self.starting_boards.generateStartingBoard()
        
    def printBoard(self):
        for row in self.grid:
            print(row)
            
    def displayBoard(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != '_':
                    txt = font.render(self.grid[i][j], True, "black", "white")
                    screen.blit(txt, (j * 100 + 50 - txt.get_rect().width / 2, i * 100 + 50 - txt.get_rect().height / 2))
                    
    def check(self, array):
        array = [int(x) for x in array if x != '_']
        array.sort()
        return array == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def checkNotValid(self, array):
        array = [int(x) for x in array if x != '_']
        array.sort()
        return array != [1, 2, 3, 4, 5, 6, 7, 8, 9] and len(array) == 9
    
    def checkrow(self, row):
        array = self.grid[row]
        if self.check(array):
            for col in range(9):
                txt = font.render(self.grid[row][col], True, "green", "white")
                screen.blit(txt, (col * 100 + 50 - txt.get_rect().width / 2, row * 100 + 50 - txt.get_rect().height / 2))
        if self.checkNotValid(array):
            for col in range(9):
                txt = font.render(self.grid[row][col], True, "red", "white")
                screen.blit(txt, (col * 100 + 50 - txt.get_rect().width / 2, row * 100 + 50 - txt.get_rect().height / 2))
        return self.check(array)
    
    def checkcol(self, col):
        array = [self.grid[i][col] for i in range(9)]
        if self.check(array):
            for row in range(9):
                txt = font.render(self.grid[row][col], True, "green", "white")
                screen.blit(txt, (col * 100 + 50 - txt.get_rect().width / 2, row * 100 + 50 - txt.get_rect().height / 2))
        if self.checkNotValid(array):
            for row in range(9):
                txt = font.render(self.grid[row][col], True, "red", "white")
                screen.blit(txt, (col * 100 + 50 - txt.get_rect().width / 2, row * 100 + 50 - txt.get_rect().height / 2))

        return self.check(array)
    
    def checksquare(self, row, col):
        array = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                array.append(self.grid[row+i][col+j])
        if self.check(array):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    txt = font.render(self.grid[row+i][col+j], True, "green", "white")
                    screen.blit(txt, ((col+j) * 100 + 50 - txt.get_rect().width / 2, (row+i) * 100 + 50 - txt.get_rect().height / 2))
        if self.checkNotValid(array):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    txt = font.render(self.grid[row+i][col+j], True, "red", "white")
                    screen.blit(txt, ((col+j) * 100 + 50 - txt.get_rect().width / 2, (row+i) * 100 + 50 - txt.get_rect().height / 2))
        return self.check(array)
    
    def checkboard(self):
        won = True
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                if self.checksquare(i, j) == False:
                    won = False
        
        for i in range(9):
            if self.checkrow(i) == False or self.checkcol(i) == False:
                won = False
        
        return won

board = Board()
highlight = pygame.Rect((5, 5), (90, 90))
row, col = 0, 0

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col, row = pygame.mouse.get_pos()
            row = row // 100
            col = col // 100
        if event.type == pygame.KEYDOWN:
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
            if event.key == pygame.K_DOWN and row < 8:
                row += 1
            if event.key == pygame.K_UP and row > 0:
                row += -1
            if event.key == pygame.K_RIGHT and col < 8:
                col += 1
            if event.key == pygame.K_LEFT and col > 0:
                col += -1
            
    highlight.x = col * 100 + 5
    highlight.y = row * 100 + 5
    screen.fill((255, 255, 255))
    screen.blit(board.img, (0, 0))
    pygame.draw.rect(screen, "yellow", highlight)
    board.displayBoard()
    if board.checkboard():
        print("True")
    pygame.display.update()

pygame.quit()
