import pygame
from pygame.locals import *
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()

alarm_sound = pygame.mixer.Sound("250.wav")
alarm_sound.set_volume(0)
alarm_sound.play(-1)

'''
Purpose:
- To make the alarm screen
Parameter:
N/A
Return:
- The red light on the screen will be created
'''
class red_flash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface((1000,600)).convert()
        self.image.set_alpha(50)
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0

'''
Purpose:
- To determine how often to show the red alarm screen
Parameter:
on: Whether the alarm has been triggered or not
screen: the window that the game in played on
alarm_group: The group that contains the red flash
seconds: The number of seconds that have gone by after the latest minute
Return:
- The red alarm screen will show itself at a consistent and smooth pace
'''
def alarm(on,screen, alarm_group, seconds):
    if seconds%2 == 0:
        alarm_group.draw(screen)
        alarm_sound.set_volume(1)
    else:
        alarm_sound.set_volume(0)

