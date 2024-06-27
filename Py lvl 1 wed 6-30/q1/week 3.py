import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

apple = pygame.image.load("Apple.png")

screen.fill( (100, 100, 255) )
#screen.blit(apple, (0, 0) )

myRect1 = pygame.Rect((100, 100), (25, 25))
myRect2 = pygame.Rect((110, 100), (25, 25))

pygame.draw.rect(screen, "white", myRect1)
pygame.draw.rect(screen, "green", myRect2)

pygame.draw.polygon(screen, "white", ((0, 0), (100, 100), (100, 0)) )

print(myRect1.colliderect(myRect2))


pygame.display.update()


while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    

    
pygame.quit()
