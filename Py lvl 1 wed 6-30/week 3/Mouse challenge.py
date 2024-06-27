import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

font = pygame.font.Font("freesansbold.ttf", 32)

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
    
    screen.fill((255, 255, 255))
    x, y = pygame.mouse.get_pos()
    text = font.render(str(x) + ", " + str(y), True, "white", "black")
    screen.blit(text, (0, 0))
    pygame.display.update()
        
    
pygame.quit()
