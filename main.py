from random import randint
import pygame
from settings import *
from utils import *

#some variables
prev = 2
count = 0
killFrame = 7

pygame.init()
pygame.display.set_caption("Rip the AI")

SCREEN = initializeScreen()

#define the clock
clock = pygame.time.Clock()

#let's create our brand new car !
my_sprite = mySprite(WIDTH//2, HEIGHT//2)

#let's add some bad boyz:
ennemies = [] #array of ennemies
ennemie_type = [] #array of the type of the ennemie*
killed = []
for _ in range(MAX_ENNEMIES):
    #defining the ennemie initial pos based on the player pos
    AIx = my_sprite.x + randint(-5, 5)*((WIDTH-50)/10)
    AIy = my_sprite.y + randint(-5, 5)*((HEIGHT-65)/10)
    ennemies.append(AIsprite(AIx, AIy))
    ennemie_type.append(randint(0, 2))#defining the type of the ennemie

while 1:
    #manage the speed
    clock.tick(FRAME_RATE)
    dir_movePlayer = 'n'
    dir_moveAI = 'n'
    
    ennemy = ennemies[1]
    
    #force all events to processed
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_sprite.move('left')
                dir_movePlayer = 'left'
                my_sprite.frame = 2
            if event.key == pygame.K_RIGHT:
                my_sprite.move('right')
                dir_movePlayer = 'right'
                my_sprite.frame = 2
            if event.key == pygame.K_UP:
                my_sprite.move('up')
                dir_movePlayer = 'back'
                my_sprite.frame = 2
            if event.key == pygame.K_DOWN:
                my_sprite.move('down')
                dir_movePlayer = 'front'
                my_sprite.frame = 2
                
            #moving an ennemy with z q s d for testing the ennemy moving func
            if event.key == pygame.K_q:
                ennemy.move('left')
                dir_moveAI = 'left'
                ennemy.frame = 2
            if event.key == pygame.K_d:
                ennemy.move('right')
                dir_moveAI = 'right'
                ennemy.frame = 2
            if event.key == pygame.K_z:
                ennemy.move('up')
                dir_moveAI = 'back'
                ennemy.frame = 2
            if event.key == pygame.K_s:
                ennemy.move('down')
                dir_moveAI = 'front'
                ennemy.frame = 2
            
            if event.key == pygame.K_ESCAPE:
                pygame.quit()#close pygame
                raise SystemExit#for a system close
    
    #fill the screen with black
    SCREEN.fill(0)
    
    #detecting if we have killed an ennemy and updating killFrame for those who are alredy dead
    for ennemie in ennemies:
        if ennemie.dead and ennemie.killFrame < 7:
            ennemie.killFrame += 1
        if ennemie.x == my_sprite.x and ennemie.y == my_sprite.y :
            ennemie.dead = 1
            if ennemie.just_killed:
                ennemie.killFrame = 0
                ennemie.just_killed = 0
            
    
    draw_AISprite(SCREEN, ennemies, ennemie_type, dir_moveAI)
    draw_killed(SCREEN, ennemies)
    draw_mySprite(SCREEN, my_sprite, dir_movePlayer)

    #set the frame for the player depending on the progress in the movement
    if my_sprite.frame == 2:
        my_sprite.frame = 3
    if my_sprite.frame == 3:
        my_sprite.frame = 0
    
    #set the frame for the ennemy depending on the progress in the movement 
    if ennemy.frame == 2:
        ennemy.frame = 3
    if ennemy.frame == 3:
        ennemy.frame = 0
    
    #set the frame for the still pos
    if (my_sprite.frame == 1 or my_sprite.frame == 0) and count >= FRAME_RATE/5:
        my_sprite.frame = not my_sprite.frame
        for ennemie in ennemies:#ennemy still pos
            ennemie.frame = not ennemie.frame
        count = 0
    count += 1
    
    pygame.display.flip()