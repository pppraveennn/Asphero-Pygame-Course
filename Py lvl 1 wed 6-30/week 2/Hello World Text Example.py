import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

font = pygame.font.Font("freesansbold.ttf", 32)
text = font.render("Hello World", True, "white", "black")

runGame = True
while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    screen.blit(text, (0, 0))
    pygame.display.update()
pygame.quit()