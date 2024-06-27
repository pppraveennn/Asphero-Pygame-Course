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

appleimg = pygame.image.load("apple.png")
applerect = pygame.Rect((0, 0), (100, 100))

basketimg = pygame.image.load("basket.png")
basketrect = pygame.Rect((700, 500), (100, 100))

speed = 5
score = 0

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    applerect.y += speed

    if (applerect.y > 600):
        applerect.y = -100
        applerect.x = random.randint(0, 700)

    basketrect.x = pygame.mouse.get_pos()[0]

##    if ((applerect.x + applerect.width > basketrect.x) and
##    (applerect.x < basketrect.x + basketrect.width) and
##    (applerect.y < basketrect.y + basketrect.height) and
##    (applerect.y + applerect.height > basketrect.y)):
    if (applerect.colliderect(basketrect)):
        score += 1
        applerect.y = -100
        applerect.x = random.randint(0, 700)

    screen.fill((255, 255, 255))
    screen.blit(appleimg, (applerect.x, applerect.y))
    screen.blit(basketimg, (basketrect.x, basketrect.y))
    
    pygame.display.update()
    timer.tick(60)
    
    
pygame.quit()
