import pygame
from pygame.locals import *
'''
Purpose:
- To create keys that would be placed around the map
- Disappear upon contact
Parameter:
key_x: The horizontal location of the key
key:y: The vertical location of the key
Return:
- Keys that would be placed around the map and would disappear upon contact with the character
'''
class key(pygame.sprite.Sprite):
    def __init__(self,key_x,key_y):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load("key.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = key_y
        self.rect.left = key_x
    def update(self,x,y):
        self.rect.top += y
        self.rect.left += x

'''
Purpose:
- To create drillss that would be placed around the map
- Disappear upon contact
Parameter:
key_x: The horizontal location of the drill
key:y: The vertical location of the drill
Return:
- Drill that would be placed around the map and would disappear upon contact with the character
'''
class drill(pygame.sprite.Sprite):
    def __init__(self,drill_x,drill_y):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load("drill.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = drill_y
        self.rect.left = drill_x
    def update(self,x,y):
        self.rect.top += y
        self.rect.left += x

'''
Purpose:
- To create small icons around the map
- Disappear upon contact
Parameter:
photo: The image of the icon
x: The horizontal location of the icon
y: The vertical location of the icon
Return:
- Icons that would be placed around the map that could be clicked
'''
class icon(pygame.sprite.Sprite):
    def __init__(self,photo,top,left):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load(photo).convert()
        self.rect = self.image.get_rect()
        self.rect.top = top
        self.rect.left = left
    def update(self,x,y):
        self.rect.top += y
        self.rect.left += x
    def get_sides(self):
        left = self.rect.left
        right = self.rect.right
        top = self.rect.top
        bottom = self.rect.bottom
        return(left,right,top,bottom)

'''
Purpose:
- To display big charts of the small icons from the map so the player can read the papers
Parameter:
photo: The image of the big chart
Return:
- The big chart will draw onto the screen when the corresponding small icon is clicked so the player can read it
'''
class chart(pygame.sprite.Sprite):
    def __init__(self,photo):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load(photo).convert()
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = 0
    def get_sides(self):
        left = self.rect.left
        right = self.rect.right
        top = self.rect.top
        bottom = self.rect.bottom
        return(left,right,top,bottom)

'''
Purpose:
- To have a guard that would patrol the hall of the bank
Parameter:
N/A
Return:
- A guard will move along halls of the bank and will raise alarm if it touches the player
'''
class guard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface((285,285)).convert()
        self.image.set_alpha(50)
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.top = 615
        self.rect.left = -1600
    def update(self,x,y,guard_x,guard_y):
        self.rect.top += y + guard_y
        self.rect.left += x + guard_x

'''
Purpose:
- To create ghosts that would stalk the player
Parameter:
x: The original horizontal location of the ghost
y: The original vertical location of the ghost
Return:
- A ghost that follows the player around whereever he/she goes
'''
class ghost(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load("ghost.gif").convert_alpha()
        self.image.set_alpha(50)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
    def update(self,x,y):
        self.rect.top += y
        self.rect.left += x
    def center(self):
        return self.rect.center

'''
Purpose:
- To create an area
- When the player enters it, a sound would play
Parameter:
N/A
Return:
- An area on the map that emits a specific sound when the player collides with it
'''
class sound_Zone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface((940,380)).convert()
        self.image.set_alpha(0)
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.top = 225
        self.rect.left = -2125
    def update(self,x,y):
        self.rect.top += y
        self.rect.left += x

'''
Purpose:
- To create an area
- Gold will draw in this area when the player opens the safe
Parameter:
N/A
Return:
rect.left: The left side of the area
rect.right: the right side of the area
rect.top: The top side of the area
rect.bottom: The bottom side of the area
- An area that will display gold in its dimensions when the safe is opened
'''
class win_Zone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface((230,230)).convert()
        self.image.set_alpha(0)
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.top = 470
        self.rect.right = -2230
    def update(self,x,y):
        self.rect.top += y
        self.rect.left += x
    def sides(self):
        return(self.rect.left,self.rect.right,self.rect.top,self.rect.bottom)

'''
Purpose:
- To create an area
- Special events would occur 
Parameter:
width: The width of the area
height: The height of the area
x: The horizontal location of the area
y: The vertical location of the area
Return:
- An area where special events like enter a code or drilling a safe occur is made
'''
class safe_Zone(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface((width,height)).convert()
        self.image.set_alpha(0)
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = x
        self.rect.right = y
    def update(self,x,y):
        self.rect.bottom += y
        self.rect.right += x
    def left(self):
        return self.rect.left
    def center(self):
        return self.rect.center

'''
Purpose:
- To create an area
- Special events would occur 
Parameter:
width: The width of the area
height: The height of the area
x: The horizontal location of the area
y: The vertical location of the area
Return:
- An area where special events like enter a code or drilling a safe occur is made
'''
class leave(pygame.sprite.Sprite):
    def __init__(self,name,x,y):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load(name).convert()
        self.rect = self.image.get_rect()
        
        self.rect.center = (x,y)
    def get_sides(self):
        return(self.rect.left,self.rect.right,self.rect.top,self.rect.bottom)

'''
Purpose:
- To create an area
- To create the class for the quit button
- Return the sides of the button
Parameter:
width: The width of the area
height: The height of the area
x: The horizontal location of the area
y: The vertical location of the area
Return:
- An area where special events like enter a code or drilling a safe occur is made or click region
'''
class quit(pygame.sprite.Sprite):
    def __init__(self,name,x,y):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load(name).convert()
        self.rect = self.image.get_rect()
        
        self.rect.left = (x)
        self.rect.top = (y)
    def get_sides(self):
        return(self.rect.left,self.rect.right,self.rect.top,self.rect.bottom)

'''
Purpose:
- To display the background photo of the game
Parameter:
N/A
Return:
- The window is pasted with the background photo
'''
class board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load("maison.jpg").convert()
        self.rect = self.image.get_rect()
        
        self.rect.center = (-1500,1000)
    def update(self,x,y):
        self.rect.top +=y
        self.rect.left +=x

'''
Purpose:
- To display a flashed background photo when there is lightning
Parameter:
N/A
Return:
- The flashed background photo is pasted onto the window when lightning is triggered
'''
class board_flash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.image.load("maison_flash.jpg").convert()
        self.rect = self.image.get_rect()
        
        self.rect.center = (-1500,1000)
    def update(self,x,y):
        self.rect.top +=y
        self.rect.left +=x


