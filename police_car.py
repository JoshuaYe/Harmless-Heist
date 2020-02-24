import pygame
from pygame.locals import *
import random

'''
Purpose:
- To create the sprite of the police car
Parameter:
N/A
Return:
- The police car sprite is made to drive on the road outside th bank
'''
class police(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load("police_cruiser.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (-4500,-200)
    '''
    Purpose: To move the police car during the player's movements
    Parameter:
    x: The horizontal movement of the  police car
    y: The vertical movement of the police car
    Return:
    - The police car moves smoothly during the player's movements
    '''
    def update(self,x,y):
        self.rect.top += y
        self.rect.left += x

'''
Purpose:
- To create the driving movement of the police car and 
Parameter:
police1: The sprite and attributes of the police car
police_group: The group containing the police car
send_police: Whether the police car will be sent or not
distance_police: The distance that the police car has traveled
Return:
send_police: Whether the police car will be sent or not (reset)
police_group: The group containing the police car
distance_police: The reset distance of the police car
'''
def drive_by(police1,police_group,send_police,distance_police):
    if send_police == 1:
        send_police = 2
    if send_police > 1:
        police1.update(5,0)
        distance_police += 5
    if distance_police > 6000:
        police1.update(-6000,0)
        send_police = 0
        distance_police = 0
    return(send_police,police_group,distance_police)

'''
Purpose:
- To randomly determine whether a police car will appear or not
Parameter:
N/A
Return:
1: The police car will appear
0: The police car will not appear
'''
def random_drive():
    drive_num = 1
    drive = random.randint(0,2)
    if drive == drive_num:
        return 1
    else:
        return 0
