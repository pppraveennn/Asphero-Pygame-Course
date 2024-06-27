import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

rect1 = pygame.Rect((100, 100), (100, 100))
timer = pygame.time.Clock()


while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False 
    screen.fill((0, 0, 0))
    rect1.x += 1
    pygame.draw.rect(screen, "green", rect1)
    pygame.display.update()
    timer.tick(60)

        
    
pygame.quit()
