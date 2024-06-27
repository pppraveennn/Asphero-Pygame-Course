import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True


while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow pressed")
            if event.key == pygame.K_a:
                print("a")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    
    
pygame.quit()
