import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

pygame.quit()
            
