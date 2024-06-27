"""
Computer paddle moves
Player paddle moves
Ball moving
Ball physics/collision bouncing
Ball stays inside the screen
Score count
Start screen
End screen
Ending the game
"""

import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode([800, 600])

playerPaddle = pygame.Rect((350, 550), (100, 25))
computerPaddle = pygame.Rect((350, 25), (100, 25))

ball = pygame.Rect((300, 100), (25, 25))
ballspeedy = 3
ballspeedx = 3

score = 0

runGame = True
pygame.key.set_repeat(10)

timer = pygame.time.Clock()

def setRandomSpeed():
    x = random.randint(-6, 6)
    y = math.sqrt(49 - x * x)
    return x, y

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            if playerPaddle.x > 0 and event.key == pygame.K_LEFT:
                playerPaddle.x += -5
            if playerPaddle.x + playerPaddle.width <= 800 and event.key == pygame.K_RIGHT:
                playerPaddle.x += 5
    ball.y += ballspeedy
    ball.x += ballspeedx

    computerPaddle.x = ball.x

    if (playerPaddle.colliderect(ball)):
        ballspeedx, ballspeedy = setRandomSpeed()
        ballspeedy = -ballspeedy
        score += 1

    if (computerPaddle.colliderect(ball)):
        ballspeedx, ballspeedy = setRandomSpeed()

    if (ball.x + ball.width >= 800):
        ballspeedx = -ballspeedx
    if (ball.x <= 0):
        ballspeedx = -ballspeedx
    
    if (ball.y >= 600):
        runGame = False
    
    screen.fill((0, 0, 0))
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Score: " + str(score), True, "white", "black")
    screen.blit(text, (0, 0))
    
    pygame.draw.rect(screen, "Blue", playerPaddle)
    pygame.draw.rect(screen, "Blue", computerPaddle)
    pygame.draw.rect(screen, "Green", ball)

    pygame.display.update()
    timer.tick(60)
    
pygame.quit()
