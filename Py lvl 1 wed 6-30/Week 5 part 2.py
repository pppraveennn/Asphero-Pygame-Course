import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

rect1 = pygame.Rect((300, 300), (100, 100))
speed = 10

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect1.x += -speed
                
            if event.key == pygame.K_RIGHT:
                rect1.x += speed
                

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "green", rect1)
    pygame.display.update()

