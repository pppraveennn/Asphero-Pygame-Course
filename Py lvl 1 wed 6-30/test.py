import pygame



pygame.init()

screen = pygame.display.set_mode([400, 800])



runGame = True



player = pygame.Rect((50,50),(50,50))

box_1 = pygame.Rect((500,00),(100,100))

box_2 = pygame.Rect((500,400),(100,400))

player.y = 100

player_speedy = 5

player_accy = 3

timer = pygame.time.Clock()



START = 0

PLAYING = 1

END = 2



gameState = START



while runGame:

    for event in pygame.event.get():

        if gameState == START:

            if event.type == pygame.QUIT:

                runGame = False

        if gameState == PLAYING:

            if (event.type == pygame.MOUSEBUTTONDOWN)and(player.y >= 50 - player.height):

                player_speedy = -25



        player.y += player_speedy

        player_speedy += player_accy



        if (player.y >= 600 - player.height):

            player.y = 600 - player.height

        if (player.colliderect(box_1)):

            gameState = END

        



        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, "pink", player)

        pygame.draw.rect(screen, (164,219,232), box_1)

        pygame.draw.rect(screen, (164,219,232), box_2)

        timer.tick(60)

        pygame.display.update()

    

pygame.quit()
