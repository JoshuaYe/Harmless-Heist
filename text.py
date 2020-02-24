import pygame
from pygame.locals import *

'''
Purpose:
- To create the beginning texts on the screen
Parameter:
name: The image of the text slide
Return:
- The exact dimensions of the beginning texts will be made
'''
class screen_text(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load(name).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.rect.left = 0

'''
Purpose:
- The timeline for the beginning texts to be shown to the player
Parameter:
group: The group containing all the images of beginning text
text: The individual images of beginning text
seconds: The number of seconds that text has been playing on the screen
start: The beginning of when to show the text slide in seconds
stop: The end of when to stop the text slide in seconds
screen: the window that the game in played on
Return:
- The beginning texts will play at the beginning of the program at a consistent and understandable pace
'''
def show_text(group,text,seconds,start,stop,screen):
    if seconds > start and seconds < stop:
        group.add(text)
        group.draw(screen)
        text.kill()
