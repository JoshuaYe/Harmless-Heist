import pygame
import random
from pygame.locals import *
pygame.mixer.pre_init(22050, -16, 2,1024)
pygame.init()

clink = pygame.mixer.Sound("coin_pick.wav")
clink.set_volume(2)

'''
Purpose:
- The gold function allows the user to collect gold bars from the floor
Parameter:
N/A
Return:
- The area near the final safe will display many collectable gold bars that the player can pocket
'''
class gold(pygame.sprite.Sprite):
    '''
    Purpose:
    - To create the object of gold
    Parameter:
    N/A
    Return:
    - The gold object is made using an image of gold
    '''
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gold.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    '''
    Purpose:
    - To move the gold around when the player is stimulating movement
    Parameter:
    x: The horizontal movement of the object
    y: The vertical movement of the object
    Return:
    - The movement and placing of the gold
    '''
    def update(self,x,y):
        self.rect.left += x
        self.rect.top += y
    '''
    Purpose:
    - To make a seemless collection system of the gold money
    Parameter:
    square_group: The sprite of the player
    Return:
    - When the player collides with gold, the gold will kill itself and the user will gain $1000
    '''
    def take_money(self,square_group):
        if pygame.sprite.spritecollide(self, square_group, False):
            clink.play()
            self.kill()
            return 1000
        else:
            return 0

'''
Purpose:
- To determine the location of the gold bar
Parameter:
gold_group: a group of all the gold bars
Return:
- The gold bars are scattered in a randomly in a certain area for the user to locate and collect
'''
def win_money(sides,gold_group):
    left = sides[0]
    right = sides[1]
    top = sides[2]
    bottom = sides[3]
    for i in range(50):
        x = random.randint(left,right)
        y = random.randint(top,bottom)
        gold1 = gold(x,y)
        gold_group.add(gold1)
