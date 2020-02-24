import pygame
from pygame.locals import *
'''
Purpose:
- Function checks whether small icon page was clicked or not
- Function displays larger version page whenever the player clicks on a small icon page
Parameter:
screen: the window that the game in played on
icon: the small icon that is clicked on by the player
chart: the large page that is drawn by the function
Return:
- Draws the large, readable page on the screen
'''
def clicked(screen,icon, chart):
    c_sides = icon.get_sides()
    left = c_sides[0]
    right = c_sides[1]
    top = c_sides[2]
    bottom = c_sides[3]
    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        if x>=left and x<right and y>=top and y<=bottom:
            chart.draw(screen)
'''
Purpose:
- Function checks whether the player has clicked to leave the game or not
Parameter:
screen: the window that the game in played on
icon: the icon that is clicked on by the player
Return:
True, False
- Whether the player has clicked to leave the game or not
'''
def clicked_leave(screen,icon):
    c_sides = icon.get_sides()
    left = c_sides[0]
    right = c_sides[1]
    top = c_sides[2]
    bottom = c_sides[3]
    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        if x>=left and x<right and y>=top and y<=bottom:
            return False
        else:
            return True
    else:
        return True
