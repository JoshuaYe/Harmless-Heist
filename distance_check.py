import pygame
from pygame.locals import *

'''
Purpose:
- To determine how far the ghost is from the player to see if the chase will begin or not
Parameter:
g: The position of the ghost
s: The position of the player sprite
chase: Whether the chase has begun or not
Return:
- The chase will begin or not begin based on the distance of the ghost and the player
'''
def distance(g,s,chase):
    if (((abs(g[0]-s[0]))**2 + (abs(g[1]-s[1]))**2)**0.5) <= 300:
        return 1
    else:
        return chase

'''
Purpose:
- To determine the direction of the ghost during the chase
Parameter:
g: The position of the ghost
s: The position of the player sprite
ghost1: The ghost selected to chase the player based on distance
Return:
- The ghost will smoothly chase the user based on the distances and directions between them
'''
def chase_move(g,s,ghost1):
    if g[0] > s[0]:
        changex = -1
    elif g[0] < s[0]:
        changex = 1
    else:
        changex = 0
    if g[1] > s[1]:
        changey = -1
    elif g[1] < s[1]:
        changey = 1
    else:
        changey = 0
    ghost1.update(changex,changey)
