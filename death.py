import pygame
from pygame.locals import *
pygame.init()

my_font = pygame.font.SysFont("helvetica", 70)
my_font.set_bold(1)
my_font1 = pygame.font.SysFont("helvetica", 50)
my_font1.set_bold(1)
field_value = ""

scream = pygame.mixer.Sound("female_scream.wav")
scream.set_volume(2.5)

boo = pygame.mixer.Sound("ghostlymoan.wav")
boo.set_volume(2.5)

siren = pygame.mixer.Sound("siren.wav")
siren.set_volume(2.5)

'''
Purpose:
- Function is called whenever the player dies
Parameter:
screen: the window that the game in played on
money_total: the total amound of money that the player has at the time of its death
minutes: the amount of minutes that have past before the player died
seconds: the amount of seconds that have past since the last full minute of the player's life
Return:
- Draws a specific pop-up image for Level 1 and Level 2
- Plays a specific moan/scream for Level1 and Level 2
- Draws a specific pop-up image if the player gets caught by the police
'''
def death(screen,money_total,minutes,seconds,level):
    pygame.mixer.stop()
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.mixer.init()
    print(money_total)
    a = 'THE END'
    b = "  $"+str(money_total)
    if seconds <10:
        seconds = "0"+str(seconds)
    c = "TIME: "+str(minutes)+":"+str(seconds)
    d = str(c+b)
    if level == 2:
        dead = pygame.image.load("ghost.jpg").convert()
        scream.play()
    elif level == 1:
        dead = pygame.image.load("cartoon_ghost.png").convert()
        boo.play()
    elif level == 0:
        dead = pygame.image.load("police_lights.jpg").convert()
        siren.play()
    field1 = my_font.render(a, False, (0,90,60))
    field2 = my_font1.render(d, False, (0,90,60))
    screen.blit(dead, (0,0))

    pygame.draw.polygon(screen, (0,90,60), ((160, 340), (160, 440), (360, 440), (360, 340)))
    pygame.draw.polygon(screen, (255,255,255), ((150, 350), (150, 450), (350, 450), (350, 350)))

    pygame.draw.polygon(screen, (0,90,60), ((685, 340), (685, 440), (885, 440), (885, 340)))
    pygame.draw.polygon(screen, (255,255,255), ((675, 350), (675, 450), (875, 450), (875, 350)))
    
    font1 = pygame.font.SysFont("8-Bit-Madness", 40)
    field3 = font1.render("Main Menu", False, (0,90,60))
    field4 = font1.render("Quit", False, (0,90,60))

    screen.blit(field1, (370,50))
    screen.blit(field2, (330,200))
    screen.blit(field3, (160, 400))
    screen.blit(field4, (700, 400))
    
