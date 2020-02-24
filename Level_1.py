import pygame
import random
from pygame.locals import *
from leave import exit1
pygame.init()

##Set screen dimensions
screen_height = 1000
screen_width = 600

##Create screen
screen = pygame.display.set_mode((screen_height,screen_width))

##Background create
background = pygame.Surface(screen.get_size()).convert()
background.fill((0, 0, 0))
screen.blit(background, (0,0))

##Load Character Images
move_left = pygame.image.load('move left/survivor-move_flashlight_0.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_1.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_2.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_3.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_4.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_5.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_6.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_7.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_8.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_9.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_10.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_11.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_12.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_13.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_14.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_15.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_16.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_17.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_18.gif').convert_alpha(), pygame.image.load('move left/survivor-move_flashlight_19.gif').convert_alpha()

##Speeds
speed = 3
diag_speed = 2

##Clock
clock = pygame.time.Clock()

##Background Dimensions
back_rect = pygame.image.load("maison.jpg").convert().get_rect()
back_height = back_rect[3]
back_width = back_rect[2]

##Sounds
thunder1 = pygame.mixer.Sound("thunder.wav")  ##thunder sound
thunder1.set_volume(1)
thunder2 = pygame.mixer.Sound("thunder2.wav")
thunder2.set_volume(1)
thunders = [thunder1, thunder2]
rain = pygame.mixer.Sound("rainy.wav")
rain.set_volume(0.5)
rain.play(-1)
back = pygame.mixer.Sound("back.wav")
##back.play(-1)
boing = pygame.mixer.Sound("boing.wav")
boing.set_volume(0.8)
##Morse code
morse = pygame.mixer.Sound("morse.wav")
morse.set_volume(0)
morse.play(-1)
##Pick
pick = pygame.mixer.Sound("pick.wav")
pick.set_volume(0.9)
##Drilling
drilling = pygame.mixer.Sound("drilling.wav")
drilling.set_volume(2.0)

'''
Purpose:
- update all the created groups in the update list to new location
Parameters:
- x location, y location, update list with all the groups
Return:
- N/A
'''
def master_Update(a,b,update_List):
    for i in update_List:
        i.update(a,b)
'''
Purpose:
- clear all groups from background
Parameters:
- clear list, contains all groups to clear
Return:
- N/A
'''
def clear(clear_List):
    for a in clear_List:
        a.clear(screen,background)
'''
Purpose:
- draw all groups in list
Parameters:
- the draw list
Return:
- N/A
'''
def draw(draw_List):
    for a in draw_List:
        a.draw(screen)
'''
Purpose:
- kill all sounds in this list
Parameters:
- sounds list
Return:
- N/A
'''
def kill_sounds(sounds_list):
    for i in sounds_list:
        i.stop()

##Main Code
'''
Purpose:
- To create the first level of the game
Return:
- Level 1 is run on the pygame window
'''
def Level1(lightning_chance,lighting_time,lightning_flash,make_Walls,move_Char,key_Open,code_Open,doors,clicked,clicked_leave,distance,chase_move,money,random_money,money_score,win_money,gold,death,alarm,red_flash,screen_text,show_text,pause_game,police,drive_by,random_drive,key,drill,icon,chart,guard,ghost,sound_Zone,win_Zone,safe_Zone,leave,quit,board,board_flash):
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.mixer.init()
    code_count = 0
    key_got = 0
    drill_got = 0

    '''
    Purpose:
    - To create the character sprite
    - To give collision properties to the player
    - To allow the character sprite to move
    Parameter:
    N/A
    Return:
    - A player sprite can collide with boundaries and walls that can move smoothly around
    '''
    class square(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((85,85)).convert()
            self.image.fill((100,0,255))
            self.rect = self.image.get_rect()
            self.image = move_left[0]
    ##        self.rect.left = (screen_width/2-25)
    ##        self.rect.top = (screen_height/2-25)
            self.rect.center = (screen_height/2,screen_width/2)
        '''
        Purpose:
        - To change the sprite image while moving, and also be rotated to the appropriate direction of which the
        sprite is moving
        - Update the walkCount every time
        Paramter:
        - walkCount - to determine which image to blit
        - move_X_Y_Dir to determine the direction of movements and rotate image
        Returns:
        - returns the updated walkCount
        '''
        def sprite_image(self,walkCount,move_X_Y_Dir):
            self.image = pygame.transform.rotate(move_left[walkCount//5],45*move_X_Y_Dir[2])
            self.rect.center = (screen_height/2,screen_width/2)
            walkCount += 1
            return walkCount
        ##get the rect sides of the sprite
        '''
        Purpose:
        - To return all the side locations of the sprite's rect
        Paramter:
        N/A
        Return:
        - All the sides of the sprite (rect.left,rect.right,rect.top,rect.bottom)
        '''
        def get_sides(self):
            top = self.rect.top
            bottom = self.rect.bottom
            left = self.rect.left
            right = self.rect.right
            return(top,bottom,left,right)
        '''
        Purpose:
        - return the center of the square
        Parameters:
        N/A
        Return:
        - return the center
        '''
        def center(self):
            return self.rect.center
        def check_collision(self,x,y):
            global code_count
            master_Update(0,y,update_List)
            guard_group.update(0,y,0,0)

            
            
            wall_hit = pygame.sprite.spritecollide(self, wall_group, False)
            for wall in wall_hit:
                key_Open(door1, door2, doors, square1, key_got)
                if y > 0:
                    change = self.rect.top-wall.rect.bottom
                    
                    master_Update(0,change,update_List)
                    guard_group.update(0,change,0,0)

                    boing.play()
                elif y < 0:
                    change = self.rect.bottom-wall.rect.top
                    
                    master_Update(0,change,update_List)
                    guard_group.update(0,change,0,0)

                    boing.play()
                    
            master_Update(x,0,update_List)
            guard_group.update(x,0,0,0)

            
            wall_hit = pygame.sprite.spritecollide(self, wall_group, False)
            for wall in wall_hit:
                key_Open(door1, door2, doors, square1, key_got)
                if x > 0:
                    change = self.rect.left-wall.rect.right
                    
                    master_Update(change,0,update_List)
                    guard_group.update(change,0,0,0)

                    boing.play()
                elif x < 0:
                    change = self.rect.right-wall.rect.left
                    
                    master_Update(change,0,update_List)
                    guard_group.update(change,0,0,0)
                    
                    boing.play()
    square1=square()
    square_group = pygame.sprite.Group(square1)
    square_sides = square1.get_sides()



    k1 = key(-3400,2400)
    key_group = pygame.sprite.Group(k1)


                
    d1 = drill(750,1950)
    drill = pygame.sprite.Group(d1)


    icon1 = icon("small_chart.png",250,-1500)
    icon2 = icon("paper1.png",1240,-730)
    icon3 = icon("paper2.png",1240,-1880)
    icon4 = icon("paper3.png",1240,-1980)
    icons = [icon1,icon2,icon3,icon4]
    icon_group = pygame.sprite.Group()
    for i in icons:
        icon_group.add(i)


    chart1 = chart("chart.png")
    chart2 = chart("paper4.png")
    chart3 = chart("paper5.png")
    chart4 = chart("paper6.png")
    chart_group1 = pygame.sprite.Group(chart1)
    chart_group2 = pygame.sprite.Group(chart2)
    chart_group3 = pygame.sprite.Group(chart3)
    chart_group4 = pygame.sprite.Group(chart4)


    guard1 = guard()
    guard_group = pygame.sprite.Group(guard1)


    ghost1 = ghost(100,1000)
    ghost2 = ghost(-1000,1000)
    ghost_group = pygame.sprite.Group(ghost1,ghost2)


    szone1 = sound_Zone()
    szone_group = pygame.sprite.Group(szone1)


    wzone = win_Zone()
    wzone_group = pygame.sprite.Group(wzone)


    safe_zone1 = safe_Zone(30,230,2012,272)
    safe_zone2 = safe_Zone(230,230,470,-2250)
    safe_zone3 = safe_Zone(130,130,1650,-31)
    safe_zone4 = safe_Zone(600,600,600,1000)
    safe_zones = [safe_zone1,safe_zone2,safe_zone3,safe_zone4]
    safe_zone_group = pygame.sprite.Group()
    for i in safe_zones:
        safe_zone_group.add(i)


    Yes = leave("Yes.gif",400,300)
    leav = leave("leave.gif",400,200)
    leave_group = pygame.sprite.Group(Yes,leav)


    quit_game = quit("quit_button.gif",0,0)
    quit_group = pygame.sprite.Group(quit_game)



    board=board()
    board_group = pygame.sprite.Group(board)


    board_flash=board_flash()
    board_flash_group = pygame.sprite.Group(board_flash)

    wall_group = make_Walls(back_height, back_width)
    door1 = doors(122, 0 ,17 , -13, 733, "b","r")
    door2 = doors(217, 0, 18, -2113, 828, "b", "r")
    door3 = doors(290, 0, 8, 275, 2037, "b", "l")
    door4 = doors(90, 0, 90, -121, 1647, "b", "l")
    door5 = doors(150, 0, 17, -2115, 1647, "b", "r")
    doors = [door1, door2, door3, door4, door5]
    for i in doors:
        wall_group.add(i)
    #################################################
    money_group = pygame.sprite.Group()
    random_money(money_group,back_width,back_height,wall_group)

    gold_group = pygame.sprite.Group()

    flash = red_flash()
    alarm_group = pygame.sprite.Group()
    alarm_group.add(flash)


    intro_text_group = pygame.sprite.Group()
    intro_text1 = screen_text("intro1.png")
    intro_text2 = screen_text("intro2.png")
    intro_text3 = screen_text("intro3.png")
    intro_text4 = screen_text("intro4.png")
    intro_text5 = screen_text("intro5.png")

    update_List = [leave_group,board_group,board_flash_group,wall_group,key_group,drill,icon_group,safe_zone_group,square_group,szone_group,ghost_group,money_group,wzone_group]####################
    clear_List = [leave_group,board_group,board_flash_group,wall_group,key_group,drill,icon_group,safe_zone_group,guard_group,chart_group1,chart_group2,chart_group3,chart_group4,ghost_group,money_group,wzone_group]
    draw_List = [wall_group,guard_group,key_group,drill,safe_zone_group,money_group,ghost_group,square_group,icon_group,wzone_group]
    sounds_list = [thunder1,thunder2,rain,back,boing,morse,pick,drilling]
    
    field_value1 = '---- -- : '
    field_value2 = '------ : '

    flash_count = 0
    money_total = 0
    timer = 0
    seconds = 0
    text_sec = 0
    minutes = 0

    open_safe_time = 0

    alarm_on = 0

    pause = False

    x=0
    y=0
    walkCount = 0
    walkDir = 0
    szone = 0
    chase1 = 0
    chase2 = 0
    guard_count = 0
    guard_f = True
    guard_y = 0
    keep_going = True
    quit_the_game = True
    while keep_going:
        clock.tick(120)

                    
        timer += 1
        if timer == 120:
            seconds += 1
            if seconds == 60:
                minutes += 1
                seconds = 0
            timer = 0
            text_sec += 1

        key_hit = pygame.sprite.spritecollide(square1, key_group, False)
        if key_hit:
                key_got += 1
                pick.play()
                if k1 in key_hit:
                    k1.kill()
                elif k2 in key_hit:
                    k2.kill()

        if pygame.sprite.spritecollide(square1, drill, False):
                d1.kill()
                drill_got = 1
                pick.play()
                
        if pygame.sprite.groupcollide(square_group, szone_group, False, False):
            morse.set_volume(0.7)
            szone = 1
        else:
            morse.set_volume(0)
            szone = 0
        if guard_f == True:
            guard_x = 3
        elif guard_f == False:
            guard_x = -3
            
        guard_count += guard_x
        if guard_count >= 900:
            guard_f = False
        elif guard_count <= -410:
            guard_f = True


        ##Ghost center
        ghost1_center = ghost1.center()
        ghost2_center = ghost2.center()
        ##Square center
        square1_center = square1.center()
        ##check
        if timer % 2 == 0:
            chase1 = distance(ghost1_center,square1_center,chase1)
            if chase1 == 1:
                chase_move(ghost1_center,square1_center,ghost1)
            chase2 = distance(ghost2_center,square1_center,chase2)
            if chase2 == 1:
                chase_move(ghost2_center,square1_center,ghost2)

        ##LIGHTNING
        flash_Num = lightning_chance()
        flash_count = lighting_time(flash_Num, flash_count)

        zone_hit = pygame.sprite.spritecollide(square1, safe_zone_group, False)

        ##Check for events
        for ev in pygame.event.get():
            if ev.type==KEYUP:
                if ev.key==K_p:
                    pause = True
            elif ev.type == QUIT:
                keep_going = False
            elif ev.type == KEYDOWN and safe_zone1 in zone_hit:
                if ev.key == K_BACKSPACE and len(field_value1) > 10:
                    field_value1 = field_value1[:-1] #cut off last character
                elif len(field_value1) < 30:
                    field_value1 += ev.unicode #adds character value of key
            elif ev.type == KEYDOWN and safe_zone3 in zone_hit:
                if ev.key == K_BACKSPACE and len(field_value2) > 9:
                    field_value2 = field_value2[:-1] #cut off last character
                elif len(field_value2) < 30:
                    field_value2 += ev.unicode #adds character value of key

        ##Move Character
        move_X_Y_Dir = move_Char(speed,diag_speed,square1)
        x = move_X_Y_Dir[0]
        y = move_X_Y_Dir[1]


        for i in money_group:
            money_gain = i.take_money(square_group,1)
            money_total += money_gain

        for i in gold_group:
            gold_gain = i.take_money(square_group)
            money_total += gold_gain
        ##########################Sprite Image#############################
        if x > 0 or y > 0 or x < 0 or y < 0:
            walkCount = square1.sprite_image(walkCount,move_X_Y_Dir)
            if walkCount + 1>=95:
                walkCount = 0

            
        ##Clear sprites###############################################
        clear(clear_List)

        flash_count = lightning_flash(flash_count, screen, thunders, board_group, board_flash_group)
        guard_group.update(0,0,guard_x, guard_y)

        ##Draw sprites################################################
        draw(draw_List)

        clicked(screen,icon1,chart_group1)
        clicked(screen,icon2,chart_group2)
        clicked(screen,icon3,chart_group3)
        clicked(screen,icon4,chart_group4)

        if alarm_on == 1:
            alarm(alarm_on,screen,alarm_group,seconds)

        ###################INTRO TEXT
        show_text(intro_text_group,intro_text1,text_sec,0,6,screen)
        show_text(intro_text_group,intro_text2,text_sec,6,12,screen)
        show_text(intro_text_group,intro_text3,text_sec,12,19,screen)
        show_text(intro_text_group,intro_text4,text_sec,19,26,screen)
        if open_safe_time == 840:
            start_text = seconds
            end_text = seconds+7
        if open_safe_time >= 840:
            show_text(intro_text_group,intro_text5,text_sec,start_text,end_text,screen)


        ##Total money Display function
        money_score(money_total,screen,seconds,minutes,key_got,drill_got)

        ##Drilling sound reset
        drilling.set_volume(0)

        if safe_zone1 in zone_hit:
            code_Open(square_group, screen, field_value1)
            if field_value1 == "---- -- : save me":
                door3.kill()
                safe_zone1.kill()
                field_value1 = ''
                
        elif safe_zone2 in zone_hit and drill_got == 1:
            drilling.play()
            drilling.set_volume(2)
            open_safe_time += 1
            if open_safe_time == 840:
                safe_zone2.kill()
                update_List.insert(0,gold_group)
                clear_List.insert(0,gold_group)
                draw_List.insert(0,gold_group)
                win_sides = wzone.sides()
                win_money(win_sides,gold_group)
                
        elif safe_zone3 in zone_hit:
            code_Open(square_group, screen, field_value2)
            if field_value2 == "------ : murder":
                k2 = key(safe_zone3.left()-35,safe_zone3.center()[1])
                key_group.add(k2)
                safe_zone3.kill()
                field_value2 == ''
                
        elif safe_zone4 in zone_hit and money_total>0:
            leave_group.draw(screen)
            leave_click_yes = clicked_leave(screen,Yes)
            if leave_click_yes == False:
                keep_going = False
                kill_sounds(sounds_list)
                intro_text_group.clear(screen,background)
                pygame.display.flip()
                exit1(screen,money_total,minutes,seconds)
        ########################################

        #####PAUSE DISPLAY
        while pause == True:
           pause_game(screen)
           pygame.display.flip()
           for event in pygame.event.get():
                if event.type==KEYUP:
                    if event.key==K_p:
                        pause = False
                        
            
        ##GUARD
        if pygame.sprite.groupcollide(square_group, guard_group, False, False) or minutes > 10:
            alarm_on = 1
            chase1 = 1
            chase2 = 1
            
        elif pygame.sprite.groupcollide(square_group, ghost_group, True, False):
            print("DEAD...")
            kill_sounds(sounds_list)
            death(screen,money_total,minutes,seconds,1)
            keep_going = False

            
        pygame.display.flip()

        if keep_going == False:
            go = True
            while go:
                for ev in pygame.event.get():
                    if ev.type == QUIT:
                        keepGoing = False
                    elif ev.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos() #if left mouse is pressed
                        x = ev.pos[0]  
                        y = ev.pos[1]
                        if y > 350 and y < 450 and x > 150 and x < 350:
                            go = False
                        elif y > 350 and y < 450 and x > 675 and x <= 875:
                            pygame.quit()


