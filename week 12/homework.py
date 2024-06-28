# apples respawning
# apples falling down
# score count
# moving basket
# apple touching basket -> increase score
# end screen
# beginning screen
# images
# smooth animation
# overlapping of apples

import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True
timer = pygame.time.Clock()

# appleimg = pygame.image.load("apple.png")
# applerect = pygame.Rect((0, 0), (100, 100))

speed = 5
score = 0

class Apple:
    def __init__(self, rect, img):
        self.rect = rect
        self.img = img

    def moveDown(self):
        self.rect.y += speed

    def detectCollision(self, binrect):
        global score
        if (self.rect.colliderect(binrect)):
            score += 1
            self.rect.y = -100
            self.rect.x = random.randint(0, 700)

    def drawImg(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))
    def drawRect(self):
        pygame.draw.rect(screen, "blue", self.rect)

    def checkEndGame(self):
        global runGame
        if (self.rect.y > 600):
            runGame = False

class Basket:
    def __init__(self, rect, img):
        self.rect = rect
        self.img = img
    def drawImg(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))
    def setPos(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = 500

appleList = []
for i in range(100):
    appleList.append(Apple(pygame.Rect((0, 0), (100, 100)), pygame.image.load("week 12/apple.png")))

basketimg = pygame.image.load("week 12/basket.png")
basketrect = pygame.Rect((700, 500), (100, 100))
basket = Basket(basketrect, basketimg)


        



while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    screen.fill((255, 255, 255))
    basket.setPos()
    basket.drawImg()

    for apple in appleList:
        apple.moveDown()
        apple.detectCollision(basketrect)
        apple.checkEndGame()
        apple.drawImg()
        #apple.drawImg()
        
    
    pygame.display.update()
    timer.tick(60)
    
    
pygame.quit()
