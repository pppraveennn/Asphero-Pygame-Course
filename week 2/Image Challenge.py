import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

img = pygame.image.load("Apple.png")

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    screen.blit(img, (800/2-img.get_width()/2, 600/2-img.get_height()/2))
    pygame.display.update()
        
    
pygame.quit()
