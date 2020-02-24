import pygame
import random
from pygame.locals import *

pygame.mixer.pre_init(22050, -16, 2,1024)
pygame.init()

clink = pygame.mixer.Sound("coin_pick.wav")
clink.set_volume(1)

'''
Purpose:
- The money function allows the user to collect scattered money from the floor
Parameter:
N/A
Return:
- Money will be appear around the map which will be collectable to the player
'''
class money(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coins.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    '''
    Purpose:
    - To move the money around when the player is stimulating movement
    Parameter:
    x: The horizontal movement of the object
    y: The vertical movement of the object
    Return:
    - The movement and placing of the money
    '''
    def update(self,x,y):
        self.rect.left += x
        self.rect.top += y
    '''
    Purpose:
    - To make a seemless collection system of the scattered money
    Parameter:
    square_group: The sprite of the player
    Return:
    - When the player collides with money, the money will kill itself and the user will gain $1 - $15
    '''
    def take_money(self,square_group,level):
        if pygame.sprite.spritecollide(self, square_group, False):
            clink.play()
            self.kill()
            if level == 1:
                money = random.randint(1,15)
            elif level == 2:
                money = random.randint(1,50)
            return money
        else:
            return 0

'''
Purpose:
- To randomly scatter the money around the map without landing itself on a solid surface
Parameter:
money_group: The group conatining all scattered money bags
back_width: The width of the background
back_height: The height of the backgroun
wall_group: The group containing all solid surfaces on the map
Return:
- The money bags will be randomly scattered throughout the map for the user to collect without landing itself on a solid surface
'''
def random_money(money_group,back_width,back_height,wall_group):
    for i in range(30):
        x = random.randint(-back_width/2-1500,back_width/2-1500)
        y = random.randint(-back_height/2+1000,back_height/2+1000)
        money1 = money(x,y)
        money_group.add(money1)
        fix = pygame.sprite.spritecollideany(money1,wall_group)
        while fix != None:
            money1.kill()
            x = random.randint(-back_width/2-1500,back_width/2-1500)
            y = random.randint(-back_height/2+1000,back_height/2+1000)
            money1 = money(x,y)
            money_group.add(money1)
            fix = pygame.sprite.spritecollideany(money1,wall_group)
