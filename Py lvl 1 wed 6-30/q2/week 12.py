import pygame
import random

pygame.init()

screen = pygame.display.set_mode([800, 600])

runGame = True
objectSize = 25

class ObstaclesPair:
    def __init__(self, x, y):
        self.topRect = pygame.Rect(x, y, objectSize, objectSize)
        self.bottomRect = pygame.Rect(x, y + 100, objectSize, objectSize)
    def draw(self):
        self.bottomRect.x = self.topRect.x
        self.bottomRect.y = self.topRect.y + 150
        pygame.draw.rect(screen, (255, 255, 255), self.topRect)
        pygame.draw.rect(screen, (255, 255, 255), self.bottomRect)

obstacles = []
numSquares = int(900 / objectSize)
for i in range(numSquares):
    obstacles.append(ObstaclesPair(1000 + objectSize*i, 200))

player = pygame.Rect(100, 100, 15, 15)
player_speedy = 5

timer = pygame.time.Clock()
pygame.key.set_repeat(20)


while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.KEYDOWN:
            player_speedy = -5
        else:
            player_speedy = 5

    player.y += player_speedy

    if player.y >= 600 - player.height:
        player.y = 600 - player.height

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)

    for i in range(len(obstacles)):
        x = random.randint(1,2)
        obstacles[i].topRect.x -= 5
        if obstacles[i].topRect.x < -100:
            obstacles[i].topRect.x = 800
            if (obstacles[i].topRect.y >= 500):
                obstacles[i].topRect.y = 500 - objectSize
            elif(obstacles[i].bottomRect.y <= 100):
                obstacles[i].bottomRect.y = 200 + objectSize
            if x == 1:
                obstacles[i].topRect.y = obstacles[i-1].topRect.y + objectSize
            if x == 2:
                obstacles[i].topRect.y = obstacles[i-1].topRect.y - objectSize
        obstacles[i].draw()
        if (player.colliderect(obstacles[i].topRect)):
            runGame = True
        if (player.colliderect(obstacles[i].bottomRect)):
            runGame = True
    pygame.display.flip()
    timer.tick(60)

pygame.quit()