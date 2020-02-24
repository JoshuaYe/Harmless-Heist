import pygame
from pygame.locals import *
import random
import time
from Level_1 import Level1
from Level_2 import Level2
from Level_1 import Level1
from Level_2 import Level2
from lightning import lightning_chance
from lightning import lighting_time
from lightning import lightning_flash
from walls import make_Walls
from move import move_Char
from key import key_Open
from key import code_Open
from walls import doors
from codechart import clicked
from codechart import clicked_leave
from distance_check import distance
from distance_check import chase_move
from money_bonus import money
from money_bonus import random_money
from ingame_score import money_score
from win_money import win_money
from win_money import gold
from death import death
from alarm import alarm
from alarm import red_flash
from text import screen_text
from text import show_text
from pause import pause_game
from police_car import police
from police_car import drive_by
from police_car import random_drive
from leave import exit1
level_list = [lightning_chance,lighting_time,lightning_flash,make_Walls,move_Char,key_Open,code_Open,doors,clicked,clicked_leave,distance,chase_move,money,random_money,money_score,win_money,gold,death,alarm,red_flash,screen_text,show_text,pause_game,police,drive_by,random_drive]

pygame.init()

'''
Purpose:
- To draw the main screen onto the pygame window
Parameter:
N/A
Return:
- The main page is seemlessly rendered onto the pygame window with its background image and visuals
'''
def main():
    img = pygame.image.load("night sky.png") #load an image as a Surface
    instructions = pygame.image.load("Instructions.jpg")
    music = pygame.mixer.Sound("back.wav")
    music.play()
     
    #use image size to determine the screen size
    screen = pygame.display.set_mode(img.get_size())
    img = img.convert() #need to convert it after we have set-up the display
    #the display will not change, so we can blit & flip the display just once first
    screen.blit(img, (0,0))
    pygame.display.flip()

    font = pygame.font.SysFont("8-Bit-Madness", 80)
    font1 = pygame.font.SysFont("8-Bit-Madness", 40)
    field_value = ""
    field = font.render(field_value, True, (0,0,0))
    field1 = font.render(field_value, True, (0,0,0))
    field2 = font1.render(field_value, True, (0,0,0))
    field3 = font1.render(field_value, True, (0,0,0))
    field4 = font1.render(field_value, True, (0,0,0))
    field5 = font1.render(field_value, True, (0,0,0))
    prev_pos = (-1,-1)

    pygame.draw.polygon(screen, (10,0,30), ((160, 340), (160, 440), (360, 440), (360, 340)))
    pygame.draw.polygon(screen, (255,255,255), ((150, 350), (150, 450), (350, 450), (350, 350)))

    pygame.draw.polygon(screen, (10,0,30), ((685, 340), (685, 440), (885, 440), (885, 340)))
    pygame.draw.polygon(screen, (255,255,255), ((675, 350), (675, 450), (875, 450), (875, 350)))

    field = font.render("HARMLESS HEIST", False, (250,250,250))
    field1 = font.render("HARMLESS HEIST", False, (10,0,30))
    field2 = font1.render("Level 1", False, (0,0,0))
    field3 = font1.render("Level 2", False, (0,0,0))

    screen.blit(field1, (270, 120))
    screen.blit(field, (260, 135))
    screen.blit(field2, (200, 400))
    screen.blit(field3, (725, 400))
    pygame.display.flip()

