
import pygame
import time

from pygame.locals import MOUSEBUTTONDOWN

pygame.init()
screen = pygame.display.set_mode([800, 600])

runGame = True

font = pygame.font.Font("OpenSans.ttf",50)
font2 = pygame.font.Font("OpenSans.ttf",17)

class Card:
    def __init__(self,img,rect):
        self.img = img
        self.rect = rect
    def draw(self):
        screen.blit(self.img,(self.rect.x,self.rect.y))
       
stage = 0
clicked = False

card1 = Card(pygame.image.load("Card_1.png"),pygame.Rect((50,125),(30,50)))
card2 = Card(pygame.image.load("Card_2.png"),pygame.Rect((205,125),(30,50)))
card3 = Card(pygame.image.load("Card_3.png"),pygame.Rect((50,335),(30,50)))
card4 = Card(pygame.image.load("Card_4.png"),pygame.Rect((205,335),(30,50)))
card5 = Card(pygame.image.load("Card_5.png"),pygame.Rect((450,125),(30,50)))
card6 = Card(pygame.image.load("Card_6.png"),pygame.Rect((610,125),(30,50)))
card7 = Card(pygame.image.load("Card_7.png"),pygame.Rect((450,335),(30,50)))
card8 = Card(pygame.image.load("Card_8.png"),pygame.Rect((610,335),(30,50)))

#card1img = pygame.image.load("Card_1.png")
#card1rect = pygame.Rect((0,0),(30,50))

text1Rect = pygame.Rect((45,545),(305,35))
text2Rect = pygame.Rect((445,545),(305,35))

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
result_list = []

select1 = []
select2 = []
select3 = []

found = False



# takes in a list of 4 Cards
def draw_stack(stack):
    stack[0].rect.x = 50
    stack[0].rect.y = 125
    stack[1].rect.x = 205
    stack[1].rect.y = 125
    stack[2].rect.x = 50
    stack[2].rect.y = 335
    stack[3].rect.x = 205
    stack[3].rect.y = 335
    stack[4].rect.x = 450
    stack[4].rect.y = 125
    stack[5].rect.x = 610
    stack[5].rect.y = 125
    stack[6].rect.x = 450
    stack[6].rect.y = 335
    stack[7].rect.x = 610
    stack[7].rect.y = 335
    stack[0].draw()
    stack[1].draw()
    stack[2].draw()
    stack[3].draw()
    stack[4].draw()
    stack[5].draw()
    stack[6].draw()
    stack[7].draw()

cards = [card1, card2, card3, card4, card5, card6, card7, card8]
draw_stack(cards)



while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = True
            mouse_pos = pygame.mouse.get_pos()
        if clicked == True and stage == 0 and(text1Rect.collidepoint(mouse_pos)):
            print("aClickOne")
            select1 = [1, 2, 3, 4]
            draw_stack([card1, card5, card6, card2, card3, card7, card8, card4])
            stage += 1
            clicked = False
        if clicked == True and stage == 1 and(text1Rect.collidepoint(mouse_pos)):
            print("bClickTwo")
            select2 = [1, 5, 6, 2]
            draw_stack([card7, card5, card3, card1, card8, card6, card4, card2])
            stage += 1
            clicked = False
        if clicked == True and stage == 0 and(text2Rect.collidepoint(mouse_pos)):
            print("ClickOne")
            select1 = [5, 6, 7, 8]
            draw_stack([card1, card5, card6, card2, card3, card7, card8, card4])
            stage += 1
            clicked = False
        if clicked == True and stage == 1 and(text2Rect.collidepoint(mouse_pos)):
            print("ClickTwo")
            select2 = [3, 7, 8, 4]
            draw_stack([card7, card5, card3, card1, card8, card6, card4, card2])
            stage += 1
            clicked = False
        # next stage (that I added)
        if clicked == True and stage == 2 and(text1Rect.collidepoint(mouse_pos)):
            select3 = [7, 5, 3, 1]
            # redefine the lists as sets, which do not contain repeated values
            select1 = set(select1)
            select2 = set(select2)
            select3 = set(select3)
            # intersection will find the unique number that is common to all sets
            final_set = select1.intersection(select2, select3)
            # the set only contains 1 number now. This will set that number to final_value
            for x in final_set:
                final_value = x
            print(x)
        if clicked == True and stage == 2 and(text2Rect.collidepoint(mouse_pos)):
            select3 = [8, 6, 4, 2]
            # redefine the lists as sets, which do not contain repeated values
            select1 = set(select1)
            select2 = set(select2)
            select3 = set(select3)
            # intersection will find the unique number that is common to all sets
            final_set = select1.intersection(select2, select3)
            # the set only contains 1 number now. This will set that number to final_value
            for x in final_set:
                final_value = x
            print(x)
            
            

           
    # screen.fill((0,0,0))
    

    pygame.draw.rect(screen, "white", text1Rect)
    pygame.draw.rect(screen, "white", text2Rect)
    title_text = font.render(" The Card Trick ", True,"white")
    screen.blit(title_text, (215,30))
    select_text1 = font2.render("Click here if your card is in this pile!", True, "black")
    screen.blit(select_text1, (50,550))
    select_text2 = font2.render("Click here if your card is in this pile!", True, "black")
    screen.blit(select_text2, (450,550))
 
    pygame.display.update()
pygame.quit()
