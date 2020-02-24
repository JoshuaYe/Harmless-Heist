import pygame
from pygame.locals import *
pygame.init()

my_font = pygame.font.SysFont("helvetica", 70)
my_font.set_bold(1)
my_font1 = pygame.font.SysFont("helvetica", 50)
my_font1.set_bold(1)
field_value = ""

sparkle = pygame.mixer.Sound("sparkle.wav")
sparkle.set_volume(2)

music = pygame.mixer.Sound("back.wav")

'''
Purpose:
- Function is called whenever the player indicates that he/she wants to leave
Parameter:
screen: the window that the game in played on
money_total: the total amound of money that the player has at the time of its death
minutes: the amount of minutes that have past before the player died
seconds: the amount of seconds that have past since the last full minute of the player's life
level: indicates which set of images and sounds to play
Return:
- Draws a gold image with a sparkly sound if the player wins
- Draws night sky image with an eerie sound if player does not win or die
'''
def exit1(screen,money_total,minutes,seconds):
    pygame.mixer.stop()
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.mixer.init()
    if money_total < 50000:
        night = pygame.image.load("night sky.png").convert()
        screen.blit(night, (0,0))
        music.play(-1)
        a = 'GOODBYE'
        field1 = my_font.render(a, False, (0,90,60))
        screen.blit(field1, (340,50))
    elif money_total >= 5000:
        win = pygame.image.load("win_screen.jpg").convert()
        screen.blit(win, (0,0))
        sparkle.play(1)
        a = 'YOU WON!'
        field1 = my_font.render(a, False, (0,90,60))
        screen.blit(field1, (370,50))
    b = "  $"+str(money_total)
    if seconds <10:
        seconds = "0"+str(seconds)
    c = "TIME: "+str(minutes)+":"+str(seconds)
    d = str(c+b)
    field2 = my_font1.render(d, False, (0,90,60))
    
    pygame.draw.polygon(screen, (0,90,60), ((160, 340), (160, 440), (360, 440), (360, 340)))
    pygame.draw.polygon(screen, (255,255,255), ((150, 350), (150, 450), (350, 450), (350, 350)))

    pygame.draw.polygon(screen, (0,90,60), ((685, 340), (685, 440), (885, 440), (885, 340)))
    pygame.draw.polygon(screen, (255,255,255), ((675, 350), (675, 450), (875, 450), (875, 350)))
    
    font1 = pygame.font.SysFont("8-Bit-Madness", 40)
    field3 = font1.render("Main Menu", False, (0,90,60))
    field4 = font1.render("Quit", False, (0,90,60))

    screen.blit(field2, (330,200))
    screen.blit(field3, (160, 400))
    screen.blit(field4, (700, 400))
    pygame.display.flip()

