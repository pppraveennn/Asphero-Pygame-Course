import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True
font = pygame.font.Font("freesansbold.ttf", 32)


player = pygame.Rect((100, 100), (50, 50))
player.y = 100
playerspeedy = 5
playeraccy = 1
score = 0

topObstacle = pygame.Rect((500, 0), (100, 800))
bottomObstacle = pygame.Rect((500, 0), (100, 800))

def placeObstacles():
    bottomObstacle.y = random.randint(200, 550)
    topObstacle.y = bottomObstacle.y - 200 - topObstacle.height

placeObstacles()

timer = pygame.time.Clock()

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            playerspeedy = -10

    player.y += playerspeedy
    playerspeedy += playeraccy

    topObstacle.x += -5
    bottomObstacle.x += -5

    if (topObstacle.x <= -200):
        topObstacle.x = 800
        bottomObstacle.x = 800
        placeObstacles()
        score += 1

    if (topObstacle.colliderect(player) or bottomObstacle.colliderect(player)):
        runGame = False

    if (player.y >= 600 - player.height):
        player.y = 600 - player.height

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "blue", player)
    pygame.draw.rect(screen, "black", topObstacle)
    pygame.draw.rect(screen, "black", bottomObstacle)
    text = font.render("Score: " + str(score), True, "white", "black")
    screen.blit(text, (0, 0))
    timer.tick(60)
    pygame.display.update()        
    
pygame.quit()
