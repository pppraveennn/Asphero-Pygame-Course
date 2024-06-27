import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True
timer = pygame.time.Clock()


rect1 = pygame.Rect((50, 50), (200, 200))
xspeed = 5

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        
    screen.fill((0, 0, 0))
    if (rect1.x + rect1.width >= 800):
        xspeed = -5
    elif (rect1.x <= 0):
        xspeed = 5
    rect1.x += xspeed
    pygame.draw.rect(screen, "green", rect1)
    pygame.display.update()
    timer.tick(60)

        
    
pygame.quit()
