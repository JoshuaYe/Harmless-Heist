import pygame
from pygame.locals import*
'''
Purpose:
- To allow the player to smoothly move around using arrow keys
Parameter:
speed: How fast the player sprite will move around the map for the directions of up, down, left, and right
diag_speed: How fast the player sprite will move around the map for the diagonal directions
square1: The sprite of the player
Return:
- The player sprite moves around the map smoothly and according to the user's input of pressing arrow keys
'''
def move_Char(speed,diag_speed,square1):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        x = diag_speed
        y = diag_speed
        walkDirection = 3
        square1.check_collision(x,y)
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        x = -diag_speed
        y = diag_speed
        walkDirection = 1
        square1.check_collision(x,y)
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        x = diag_speed
        y = -diag_speed
        walkDirection = 5
        square1.check_collision(x,y)
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        x = -diag_speed
        y = -diag_speed
        walkDirection = 7
        square1.check_collision(x,y)
    elif keys[pygame.K_UP]:
        x = 0
        y = speed
        walkDirection = 2
        square1.check_collision(x,y)
    elif keys[pygame.K_DOWN]:
        x = 0
        y = -speed
        walkDirection = 6
        square1.check_collision(x,y)
    elif keys[pygame.K_LEFT]:
        x = speed
        y = 0
        walkDirection = 4
        square1.check_collision(x,y)
    elif keys[pygame.K_RIGHT]:
        x = -speed
        y = 0
        walkDirection = 0
        square1.check_collision(x,y)
    else:
        x = 0
        y = 0
        walkDirection = 0
        square1.check_collision(x,y)
    return(x,y,walkDirection)
