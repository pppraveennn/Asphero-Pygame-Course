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
                    screen.blit(txt, (j * 100 + 50-txt.get_rect().width/2, i * 100 + 50-txt.get_rect().height/2))
    def check(self, array):
        array.sort()
        return array == [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
            

    screen.fill((255, 255, 255))
    screen.blit(board.img, (0, 0))
    board.displayBoard()
    pygame.display.update()


pygame.quit()


# def check(array):
#     # take in an array of length 9
#     # return true if exactly 1 of each number
#     # return false otherwise

# check([1, 2, 7, 4, 5, 6, 8, 8, 9])
