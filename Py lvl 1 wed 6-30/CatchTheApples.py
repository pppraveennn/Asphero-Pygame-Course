import sys

import pygame
import random
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()
screen = pygame.display.set_mode([600,400])
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 20)

apple = pygame.image.load("Apple.png")
applerect = pygame.Rect((0,0),(100,100))
basket = pygame.image.load("Basket.png")
basketrect = pygame.Rect((0,300),(100,100))

speed = 1
score = 0

START = 0
PLAYING = 1
END = 2

gameState = START

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            if gameState == START:
                gameState = PLAYING

    screen.fill((255, 255, 255))
    if gameState == START:
        welcome_text = font.render("Welcome to Catch the Apples! Click to play", True, (0, 0, 0))
        screen.blit(welcome_text, (115, 175))

    elif gameState == PLAYING:
        applerect.y += speed
        basketrect.x = pygame.mouse.get_pos()[0]
        
        if (applerect.y > 400):
            gameState = END

        if basketrect.colliderect(applerect):
            applerect.y = -100
            applerect.x = random.randint(0, 500)
            score += 1

        screen.blit(apple, (applerect.x, applerect.y))
        screen.blit(basket, (basketrect.x, basketrect.y))

        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    elif gameState == END:
        end_text = font.render("Game Over!", True, (0, 0, 0))
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(end_text, (115, 175))
        screen.blit(score_text, (115, 275))
    
    clock.tick(60)
    pygame.display.update()
