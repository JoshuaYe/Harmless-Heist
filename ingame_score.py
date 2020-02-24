import pygame
from pygame.locals import *

my_font = pygame.font.SysFont("helvetica", 20)
field_value = ""
field_surf = pygame.Surface((310, 35))
field_surf.fill((255,255,255))

'''
Purpose:
- Function displays the total money collected by the player, time the player has played, and inventory of the player
Parameter:
screen: the window that the game in played on
money_total: the total amound of money that the player has at the time of its death
minutes: the amount of minutes that have past before the player died
seconds: the amount of seconds that have past since the last full minute of the player's life
key_got: the amount of keys that the player has collected
drill_got: the amount of drills that the player has collected
Return:
- Small screen that shows to the user the total money collected, time played, and their inventory
'''
def money_score(money_total,screen,seconds,minutes,key_got,drill_got):
    a = "$"+str(money_total)
    if seconds <10:
        seconds = "0"+str(seconds)
    b = "  TIME: "+str(minutes)+":"+str(seconds)
    c = str(a+b)
    d = str(key_got)
    e = str(drill_got)
    key_icon = pygame.image.load("key_icon.gif").convert()
    drill_icon = pygame.image.load("drill_icon.gif").convert()
    colour = (20,200,20)
    field1 = my_font.render(c, False, (colour))
    field2 = my_font.render(d, False, (colour))
    field3 = my_font.render(e, False, (colour))

    screen.blit(field_surf, (660,10))
    screen.blit(field1, (680, 15))
    screen.blit(key_icon, (855, 20))
    screen.blit(drill_icon, (917, 15))
    screen.blit(field2, (895,15))
    screen.blit(field3, (950,15))

