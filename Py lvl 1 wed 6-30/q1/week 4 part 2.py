import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True
timer = pygame.time.Clock()

rect1 = pygame.Rect((0, 300), (100, 100))
rect2 = pygame.Rect((700, 300), (100, 100))

speed1 = 5
speed2 = -5

while runGame:
    timer.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, "green", rect2)
    pygame.draw.rect(screen, "blue", rect1)
    
    rect1.x += speed1
    rect2.x += speed2
    if (rect1.x > 700):
        speed1 = -speed1
        #speed2 = -speed2
    
    pygame.display.update()
        
    
pygame.quit()
