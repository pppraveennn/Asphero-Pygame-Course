import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

rect1 = pygame.Rect((50, 50), (200, 200))

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect1.x += 5
            if event.key == pygame.K_LEFT:
                rect1.x += -5
            if event.key == pygame.K_UP:
                rect1.y += -5
            if event.key == pygame.K_DOWN:
                rect1.y += 5
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, "green", rect1)
    pygame.display.update()
        
    
pygame.quit()
