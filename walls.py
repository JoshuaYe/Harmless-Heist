import pygame
import random
from pygame.locals import*

'''
Purpose:
- To create the vertical boundaries for the map
Parameter:
N/A
Return:
- A vertical boundary around the map 
'''
class wall_vert(pygame.sprite.Sprite):
    '''
    Purpose:
    - To create the vertical boundaries for the map
    Parameter:
    back_height: The height of the object
    back_width: The width of the object
    thick: The thickness of the object
    loc1: The location of the object, x-value
    loc2: The location of the object, y-value
    Return:
    - A boundary with collision and boundaries
    '''
    def __init__(self, back_height, back_width, thick, loc1, loc2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((thick,back_height)).convert()
        self.image.set_alpha(50)
        self.image.fill((250,0,0,20))
        self.rect = self.image.get_rect()
        self.rect.center = (loc1,loc2)
    '''
    Purpose:
    - To move the boundary around when the player is stimulating movement
    Parameter:
    x: The horizontal movement of the object
    y: The vertical movement of the object
    Return:
    - The movement and placing of the boundary
    '''        
    def update(self,x,y):
        self.rect.top +=y
        self.rect.left +=x

'''
Purpose:
- To create the horizontal boundaries for the map
Parameter:
N/A
Return:
- A horizontal boundary around the map 
'''
class wall_hori(pygame.sprite.Sprite):
    '''
    Purpose:
    - To create the horizontal boundaries for the map
    Parameter:
    back_height: The height of the object
    back_width: The width of the object
    thick: The thickness of the object
    loc1: The location of the object, x-value
    loc2: The location of the object, y-value
    Return:
    - A boundary with collision and boundaries
    '''
    def __init__(self, back_height, back_width, thick, loc1, loc2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((back_width, thick)).convert()
        self.image.set_alpha(50)
        self.image.fill((250,0,0,20))
        self.rect = self.image.get_rect()
        self.rect.center = (loc1,loc2)
    '''
    Purpose:
    - To move the boundary around when the player is stimulating movement
    Parameter:
    x: The horizontal movement of the object
    y: The vertical movement of the object
    Return:
    - The movement and placing of the boundary
    '''           
    def update(self,x,y):
        self.rect.top +=y
        self.rect.left +=x

'''
Purpose:
- To create the vertical walls for the map
Parameter:
N/A
Return:
- A vertical wall with collision and boundaries
'''
class wall_vert_w(pygame.sprite.Sprite):
    '''
    Purpose:
    - To create the vertical walls for the map
    Parameter:
    back_height: The height of the object
    back_width: The width of the object
    thick: The thickness of the object
    loc1: The location of the object, x-value
    loc2: The location of the object, y-value
    tb: The top or bottom surface of the object
    lr: The left or right surface of the object
    Return:
    - A wall with collision and boundaries
    '''
    def __init__(self, back_height, back_width, thick, loc1, loc2, tb, lr):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((thick,back_height)).convert()
        self.image.set_alpha(0)
        self.image.fill((250,0,0,20))
        self.rect = self.image.get_rect()

        if tb == "b":
            self.rect.bottom = (loc2)
        elif tb == "t":
            self.rect.top = (loc2)
        if lr == "r":
            self.rect.right = (loc1)
        elif lr == "l":
            self.rect.left = (loc1)
    '''
    Purpose:
    - To move the wall around when the player is stimulating movement
    Parameter:
    x: The horizontal movement of the object
    y: The vertical movement of the object
    Return:
    - The movement and placing of the wall
    '''               
    def update(self,x,y):
        self.rect.top +=y
        self.rect.left +=x

'''
Purpose:
- To create the horizontal walls for the map
Parameter:
N/A
Return:
- A horizontal wall with collision and boundaries
'''
class wall_hori_w(pygame.sprite.Sprite):
    '''
    Purpose:
    - To create the horizontal walls for the map
    Parameter:
    back_height: The height of the object
    back_width: The width of the object
    thick: The thickness of the object
    loc1: The location of the object, x-value
    loc2: The location of the object, y-value
    tb: The top or bottom surface of the object
    lr: The left or right surface of the object
    Return:
    - A wall with collision and boundaries
    '''    
    def __init__(self, back_height, back_width, thick, loc1, loc2, tb, lr):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((back_width, thick)).convert()
        self.image.set_alpha(0)
        self.image.fill((250,0,0,20))
        self.rect = self.image.get_rect()

        if tb == "b":
            self.rect.bottom = (loc2)
        elif tb == "t":
            self.rect.top = (loc2)
        if lr == "l":
            self.rect.left = (loc1)
        elif lr == "r":
            self.rect.right = (loc1)
    '''
    Purpose:
    - To move the wall around when the player is stimulating movement
    Parameter:
    x: The horizontal movement of the object
    y: The vertical movement of the object
    Return:
    - The movement and placing of the wall
    '''              
    def update(self,x,y):
        self.rect.top +=y
        self.rect.left +=x

'''
Purpose:
- To create the doors for the map
Parameter:
N/A
Return:
- A door with collision and boundaries
'''
class doors(pygame.sprite.Sprite):
    '''
    Purpose:
    - To create the doors for the map
    Parameter:
    back_height: The height of the object
    back_width: The width of the object
    thick: The thickness of the object
    loc1: The location of the object, x-value
    loc2: The location of the object, y-value
    tb: The top or bottom surface of the object
    lr: The left or right surface of the object
    Return:
    - A door with collision and boundaries
    '''    
    def __init__(self, back_height, back_width, thick, loc1, loc2, tb, lr):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((thick,back_height)).convert()
        self.image.fill((102,51,0))
        self.rect = self.image.get_rect()

        if tb == "b":
            self.rect.bottom = (loc2)
        elif tb == "t":
            self.rect.top = (loc2)
        if lr == "r":
            self.rect.right = (loc1)
        elif lr == "l":
            self.rect.left = (loc1)
    '''
    Purpose:
    - To move the door around when the player is stimulating movement
    Parameter:
    x: The horizontal movement of the object
    y: The vertical movement of the object
    Return:
    - The movement and placing of the door
    '''               
    def update(self,x,y):
        self.rect.top +=y
        self.rect.left +=x

'''
Purpose:
- To create the boundaries, walls, and doors of the game map
Parameter:
back_height: The height of map's boundaries
back_width: The width of the map's boundaries
Return:
wall_group: The group containing all of the map's boundaries, walls, and doors
'''        
def make_Walls(back_height, back_width):
    ##Walls
    wall1 = wall_vert(back_height, back_width, 10, ((back_width/2)-1500), 1000)
    wall2 = wall_vert(back_height, back_width, 10, ((-back_width/2)-1500), 1000)
    wall3 = wall_hori(back_height, back_width, 10, -1500, ((back_height/2)+1000))
    wall4 = wall_hori(back_height, back_width, 10, -1500, ((-back_height/2)+1000))
    wall5 = wall_hori_w(0, 2482, 15, -2495, 1663, "b", "l")
    wall6 = wall_vert_w(1440, 0, 15, -2480, 1663, "b", "r")
    wall7 = wall_hori_w(0, 1320, 15, -2495, 233, "b", "l")
    wall8 = wall_vert_w(393, 0, 15, -1175, 218, "t", "r")
    wall9 = wall_hori_w(0, 1177, 15, -1190, 611, "b", "l")
    wall10 = wall_vert_w(925, 0, 15, -13, 1663, "b", "r")
    wall11 = wall_hori_w(0, 815, 15, -2130, 611, "b", "l")
    wall12 = wall_hori_w(0, 926, 15, -2130, 923, "b", "l")
    wall13 = wall_hori_w(0, 926, 15, -1080, 923, "b", "l")
    wall14 = wall_vert_w(393, 0, 15, -2130, 218, "t", "l")
    wall15 = wall_vert_w(695, 0, 15, -2130, 829, "t", "l")
    wall16 = wall_vert_w(616, 0, 15, -1080, 1524, "b", "l")
    safe1 = wall_hori_w(0, 200, 193, -2490, 233, "t", "l")
    safe2 = wall_hori_w(0, 105, 105, -13, 1663, "b", "r")
    box1 = wall_hori_w(0, 350, 117, -1535, 233, "t", "l")
    box2 = wall_hori_w(0, 120, 110, -2130, 233, "t", "l")
    desk1 = wall_hori_w(0, 100, 402, -1750, 920, "t", "l")
    desk2 = wall_hori_w(0, 350, 105, -2010, 1217, "t", "l")
    desk3 = wall_hori_w(0, 100, 402, -710, 920, "t", "l")
    desk4 = wall_hori_w(0, 350, 105, -970, 1217, "t", "l")
    chair1 = wall_hori_w(0, 74, 74, -1865, 1072, "t", "l")
    chair2 = wall_hori_w(0, 74, 74, -845, 1072, "t", "l")
    bush1 = wall_hori_w(0, 2613, 144, -2562, 2075, "t", "l")
    bush2 = wall_vert_w(1647, 0, 148, -3162, 223, "t", "l")
    car1 = wall_vert_w(437, 0, 170, -916, -30, "t", "l")
    shed_wall1 = wall_hori_w(0, 645, 13, 275, 1725, "t", "l")
    shed_wall2 = wall_vert_w(328, 0, 13, 908, 1725, "t", "l")
    shed_wall3 = wall_hori_w(0, 645, 13, 275, 2040, "t", "l")
    shed_wall4 = wall_vert_w(35, 0, 5, 275, 1725, "t", "l")
    shed_wall5 = wall_vert_w(28, 0, 5, 275, 2040, "b", "l")
    start_car = wall_vert_w(437, 0, 370, 550, 50, "t", "l")
    walls = [wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,safe1,safe2,box1,box2,desk1,desk2,desk3,desk4,chair1,chair2,bush1,bush2,car1,shed_wall1,shed_wall2,shed_wall3,shed_wall4,shed_wall5,start_car]
    wall_group = pygame.sprite.Group()
    for i in walls:
        wall_group.add(i)
    
    return wall_group
