import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True
font = pygame.font.Font("freesansbold.ttf", 64)
tl = font.render("TL", True, "white", "black")
tr = font.render("TR", True, "white", "black")
bl = font.render("BL", True, "white", "black")
br = font.render("BR", True, "white", "black")

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    screen.blit(tl, (0, 0))
    screen.blit(tr, (700, 0))
    screen.blit(bl, (0, 535))
    screen.blit(br, (700, 535))
    pygame.display.update()
    
pygame.quit()