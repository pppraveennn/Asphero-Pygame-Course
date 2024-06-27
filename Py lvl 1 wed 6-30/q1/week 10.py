import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

player = pygame.Rect((100, 100), (100, 100))
player.y = 100
playerspeedy = 5
playeraccy = 2

obstacle = pygame.Rect((800, 500), (100, 100))

timer = pygame.time.Clock()

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if (event.type == pygame.MOUSEBUTTONDOWN and player.y + player.height >= 600):
            playerspeedy = -50

    player.y += playerspeedy
    playerspeedy += playeraccy

    if (player.y >= 600 - player.height):
        player.y = 600 - player.height

    obstacle.x += -10
    if (obstacle.x <= -200):
        obstacle.x = 800
    if (obstacle.colliderect(player)):
        runGame = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "blue", player)
    pygame.draw.rect(screen, "red", obstacle)
    timer.tick(60)
    pygame.display.update()        
    
pygame.quit()
