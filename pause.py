import pygame
from pygame.locals import *

'''
Purpose:
- To display the pause screen visual when the player pausing the game
Parameter:
screen: the window that the game in played on
Return:
- The pause visual is drawn onto the screen after th user pauses
'''
def pause_game(screen):
    my_font = pygame.font.SysFont("helvetica", 100)  
    field = my_font.render("PAUSED", False, (255,255,255))
    screen.blit(field, (300,230))
