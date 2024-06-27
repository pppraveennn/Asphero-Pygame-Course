import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

rect1 = pygame.Rect((100, 100), (100, 100))

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
    screen.fill((0, 0, 0))
    rect1.x, rect1.y = pygame.mouse.get_pos()
    pygame.draw.rect(screen, "green", rect1)
    pygame.display.update()

        
    
pygame.quit()
