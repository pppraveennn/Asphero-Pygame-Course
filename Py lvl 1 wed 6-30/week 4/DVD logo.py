import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True
timer = pygame.time.Clock()


rect1 = pygame.Rect((50, 50), (150, 50))
xspeed = 5
yspeed = 5

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        
    screen.fill((0, 0, 0))
    if (rect1.x + rect1.width >= 800):
        xspeed = -random.randint(1, 5)
    elif (rect1.x <= 0):
        xspeed = random.randint(1, 5)
    if (rect1.y + rect1.height > 600):
        yspeed = -random.randint(1, 5)
    elif (rect1.y <= 0):
        yspeed = random.randint(1, 5)

    rect1.x += xspeed
    rect1.y += yspeed
    pygame.draw.rect(screen, "green", rect1)
    pygame.display.update()
    timer.tick(60)

        
    
pygame.quit()
