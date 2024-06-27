import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

player = pygame.Rect((100, 100), (100, 100))
player.y = 100
playerspeedy = 0
playeraccy = 2

timer = pygame.time.Clock()

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if (event.type == pygame.MOUSEBUTTONDOWN and player.y + player.height >= 600):
            playerspeedy = -20

    player.y += playerspeedy
    playerspeedy += playeraccy

    if (player.y >= 600 - player.height):
        player.y = 600 - player.height

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "blue", player)
    timer.tick(60)
    pygame.display.update()        
    
pygame.quit()
