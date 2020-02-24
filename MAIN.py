'''
Programmers: Bryan Kikuta, Joshua Ye
For: ICS3U1-03 Summative
Purpose: To create the Harmless Heist game
Date: Tuesday, May 28, 2019
'''
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
from main_screen import main

from classes import key
from classes import drill
from classes import icon
from classes import chart
from classes import guard
from classes import ghost
from classes import sound_Zone
from classes import win_Zone
from classes import safe_Zone
from classes import leave
from classes import quit
from classes import board
from classes import board_flash
level_list = [lightning_chance,lighting_time,lightning_flash,make_Walls,move_Char,key_Open,code_Open,doors,clicked,clicked_leave,distance,chase_move,money,random_money,money_score,win_money,gold,death,alarm,red_flash,screen_text,show_text,pause_game,police,drive_by,random_drive,key,drill,icon,chart,guard,ghost,sound_Zone,win_Zone,safe_Zone,leave,quit,board,board_flash]

#use image size to determine the screen size
img = pygame.image.load("night sky.png")
instructions = pygame.image.load("Instructions.jpg")
screen = pygame.display.set_mode(img.get_size())

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
clock = pygame.time.Clock()
keep_going = True
main()

#Main game loop
while keep_going:
    clock.tick(30)
    main()
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keepGoing = False5
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #if left mouse is pressed
            x = ev.pos[0]  
            y = ev.pos[1]
            if y > 350 and y < 450 and x > 150 and x < 350:
                screen.blit(instructions,(0,0))
                pygame.display.flip()
                time.sleep(10)
                screen.blit(img, (0,0))
                pygame.display.flip()
                Level1(lightning_chance,lighting_time,lightning_flash,make_Walls,move_Char,key_Open,code_Open,doors,clicked,clicked_leave,distance,chase_move,money,random_money,money_score,win_money,gold,death,alarm,red_flash,screen_text,show_text,pause_game,police,drive_by,random_drive,key,drill,icon,chart,guard,ghost,sound_Zone,win_Zone,safe_Zone,leave,quit,board,board_flash)
            
            elif y > 350 and y < 450 and x > 675 and x <= 875:
                screen.blit(instructions,(0,0))
                pygame.display.flip()
                time.sleep(10)
                screen.blit(img, (0,0))
                pygame.display.flip()
                Level2(lightning_chance,lighting_time,lightning_flash,make_Walls,move_Char,key_Open,code_Open,doors,clicked,clicked_leave,distance,chase_move,money,random_money,money_score,win_money,gold,death,alarm,red_flash,screen_text,show_text,pause_game,police,drive_by,random_drive,key,drill,icon,chart,guard,ghost,sound_Zone,win_Zone,safe_Zone,leave,quit,board,board_flash)

