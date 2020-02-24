import pygame
from pygame.locals import *
'''
Purpose:
- To kill the appropriate door if the user collides with it with the right key
Parameter:
door1: the main bank door that requires a key
door2: the interior bank door that requires a second key
doors: the group doors in the map
square1: the player sprite
key_got: the amount of keys that the player has in possession
Return:
- The appropriate door is killed based on collision with the player and the number of keys
'''
def key_Open(door1, door2, doors, square1, key_got):
    gets_hit = pygame.sprite.spritecollide(square1, doors, False)
    if door1 in gets_hit and key_got == 1:
        door1.kill()
    elif door2 in gets_hit and key_got == 2:
        door2.kill()
'''
Purpose:
- To display the text to prompt the player to type in a code
Parameter:
square_group: the sprite of the player
screen: the window that the game in played on
field_value: holds the original text that is displayed to the user; the player will add onto the field by typing
Return:
field_value: What is initially displayed on the screen for typing
'''
def code_Open(square_group, screen, field_value):
    my_font = pygame.font.SysFont("helvetica", 40)
    field = my_font.render("Enter the code:", False, (255,255,255))
    field2 = my_font.render(field_value, False, (255,255,255))
    screen.blit(field, (0, 0))
    screen.blit(field2,(0, 40))
    
    return field_value
