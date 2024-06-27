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

font = pygame.font.Font("freesansbold.ttf", 32)
score = 0

appleimg = pygame.image.load("week 5/Apple.png")
applerect = appleimg.get_rect()

basketimg = pygame.image.load("week 5/basket.png")
basketrect = basketimg.get_rect()
basketrect.y = 500

speed = 5
score = 0

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    applerect.y += speed

    if (applerect.y > 600):
        runGame = False

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
    scoretxt = font.render("Score: " + str(score), True, "black", "white")
    screen.blit(scoretxt, (0, 0))
    
    pygame.display.update()
    timer.tick(60)
    
    
pygame.quit()
