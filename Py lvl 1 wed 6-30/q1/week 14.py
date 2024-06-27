import pygame
import time

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

myRect = pygame.Rect((300, 200), (200, 100))

stage = 0
clicked = False

timer = pygame.time.Clock()

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = True
            mouse_pos = pygame.mouse.get_pos()
        if stage == 0 and clicked == True and (myRect.collidepoint(mouse_pos)):
                print("Click1")
                stage += 1
                clicked = False
        if stage == 1 and clicked == True and (myRect.collidepoint(mouse_pos)):
            print("Click2")
            stage += 1
            clicked = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, "blue", myRect)
    pygame.display.update()
    timer.tick(60)
        
    
pygame.quit()
