import pygame
from pygame.locals import *
pygame.init()
import random

'''
Purpose:
- To determine a number for whether lightning will strike or not
Parameter:
N/A
Return:
flash_Num: A number will decides whether lightning will strike or not
'''
def lightning_chance():
    flash_Num = random.randint(0,1500)
    return flash_Num

'''
Purpose:
- To determine whether the lightning will flash or not
Parameter:
flash_Num: A random number
flash_count: The number of times lightning has striked
Return:
1: Lightning has striked once
flash_count: The number of times lightning has striked
'''
def lighting_time(flash_Num, flash_count):
    if flash_Num == 50:
        return 1
    else:
        return flash_count

'''
Purpose:
- To flash the lightning onto the screen
Parameter:
flash_count: The number of times lilghtning has striked
screen: the window that the game in played on
thunders: the sound files for thunder
board_group: The group containing the background photo
board_flash_group: The  group containing the flashed background photo for lightning
Return:
flash_count: The number of times lightning has striked
- Thunder and lightning will be stiumlated by flashing on the screen and sounds of thunder
'''    
def lightning_flash(flash_count, screen, thunders, board_group, board_flash_group):
    if flash_count < 1 or flash_count > 15: 
        board_group.draw(screen)
        return flash_count
    
    elif flash_count >= 1 and flash_count <= 15:
        if flash_count == 1:
            thunder_Num = random.randint(0,len(thunders)-1)
            thunders[thunder_Num].play()
        if flash_count < 8 or flash_count > 12:
            board_flash_group.draw(screen)
        else:
            board_group.draw(screen)
        flash_count+=1
        return flash_count
