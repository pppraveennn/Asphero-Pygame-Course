import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

rect1 = pygame.Rect((100, 500), (100, 100))

yspeed = 0
flipped = False

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if (flipped == False):
                    yspeed = -1
                if (flipped):
                    yspeed = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            flipped = not flipped

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "green", rect1)
    rect1.y += yspeed
    if (rect1.y < 100) and (flipped == False):
        yspeed = 1
    if (flipped == True) and (rect1.y > 400):
        yspeed = -1
    
    if (rect1.y > 600 - rect1.height) and (flipped == False):
        yspeed = 0
    if (rect1.y < 0) and (flipped):
        yspeed = 0
    
    pygame.display.update()
    
pygame.quit()
