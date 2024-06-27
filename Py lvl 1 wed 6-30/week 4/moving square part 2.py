import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True
timer = pygame.time.Clock()


rect1 = pygame.Rect((50, 50), (200, 200))
xspeed = 0
yspeed = 0

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xspeed = 5
                yspeed = 0
            if event.key == pygame.K_LEFT:
                xspeed = -5
                yspeed = 0
            if event.key == pygame.K_UP:
                yspeed = -5
                xspeed = 0
            if event.key == pygame.K_DOWN:
                yspeed = 5
                xspeed = 0
    screen.fill((0, 0, 0))
    rect1.x += xspeed
    rect1.y += yspeed
    pygame.draw.rect(screen, "green", rect1)
    pygame.display.update()
    timer.tick(60)

        
    
pygame.quit()
