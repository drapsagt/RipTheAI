import pygame
from settings import *
import random

#function to start screen
def initializeScreen():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.flip()
    return SCREEN

#function to display the screen
def draw_mySprite(screen, mySprite, move):
    if mySprite.frame == 2:#premier mouvement
        if move == "front":
            screen.blit(FRONT0, (mySprite.x-23, (mySprite.y-30)-((HEIGHT-65)/10)*2/3))#on affiche à 1/3 du trajet
        if move == "back":
            screen.blit(BACK0, (mySprite.x-23, (mySprite.y-30)+((HEIGHT-65)/10)*2/3))#on affiche à 1/3 du trajet
        if move == "right":
            screen.blit(RIGHT0, ((mySprite.x-23)-((WIDTH-50)/10*2/3), mySprite.y-30))#on affiche à 1/3 du trajet
        if move == "left":
            screen.blit(LEFT0, ((mySprite.x-23)+((WIDTH-50)/10*2/3), mySprite.y-30))#on affiche à 1/3 du trajet
            
    if mySprite.frame == 3:#second mouvement
        if move == "front":
            screen.blit(FRONT1, (mySprite.x-23, (mySprite.y-30)-((HEIGHT-65)/10)*1/3))#on affiche à 2/3 du trajet
        if move == "back":
            screen.blit(BACK1, (mySprite.x-23, (mySprite.y-30)+((HEIGHT-65)/10)*1/3))#on affiche à 2/3 du trajet
        if move == "right":
            screen.blit(RIGHT1, ((mySprite.x-23)-((WIDTH-50)/10*1/3), mySprite.y-30))#on affiche à 2/3 du trajet
        if move == "left":
            screen.blit(LEFT1, ((mySprite.x-23)+((WIDTH-50)/10*1/3), mySprite.y-30))#on affiche à 2/3 du trajet
                              
    elif mySprite.frame == 1 or mySprite.frame == 0:
        screen.blit(pygame.image.load(f".\\sprites\\doom_guy\\still{int(mySprite.frame)}.png"), (mySprite.x-23, mySprite.y-30))


        
    
def draw_AISprite(screen, AISprites, type, move):
    for sprite in AISprites:
        if not sprite.dead:
            if sprite.frame == 2:#premier mouvement
                if move == "front":
                    screen.blit(FRONTI0, (sprite.x-23, (sprite.y-30)-((HEIGHT-65)/10)*2/3))#on affiche à 1/3 du trajet
                if move == "back":
                    screen.blit(BACKI0, (sprite.x-23, (sprite.y-30)+((HEIGHT-65)/10)*2/3))#on affiche à 1/3 du trajet
                if move == "right":
                    screen.blit(RIGHTI0, ((sprite.x-23)-((WIDTH-50)/10*2/3), sprite.y-30))#on affiche à 1/3 du trajet
                if move == "left":
                    screen.blit(LEFTI0, ((sprite.x-23)+((WIDTH-50)/10*2/3), sprite.y-30))#on affiche à 1/3 du trajet
                    
            if sprite.frame == 3:#second mouvement
                if move == "front":
                    screen.blit(FRONTI1, (sprite.x-23, (sprite.y-30)-((HEIGHT-65)/10)*1/3))#on affiche à 2/3 du trajet
                if move == "back":
                    screen.blit(BACKI1, (sprite.x-23, (sprite.y-30)+((HEIGHT-65)/10)*1/3))#on affiche à 2/3 du trajet
                if move == "right":
                    screen.blit(RIGHTI1, ((sprite.x-23)-((WIDTH-50)/10*1/3), sprite.y-30))#on affiche à 2/3 du trajet
                if move == "left":
                    screen.blit(LEFTI1, ((sprite.x-23)+((WIDTH-50)/10*1/3), sprite.y-30))#on affiche à 2/3 du trajet
                    
            elif sprite.frame == 1 or sprite.frame == 0:
                screen.blit(pygame.image.load(f".\\sprites\\imps\\still{type[AISprites.index(sprite)]}{int(sprite.frame)}.png"), (sprite.x-23, sprite.y-30))
            
def draw_killed(screen, deaths):
    for sprite in deaths:
        if sprite.dead:
            screen.blit(pygame.image.load(f".\\sprites\\imps\\death{sprite.killFrame}.png"), (sprite.x-30, sprite.y-30))

def updateKillFrame(ennemies):
    for ennemie in ennemies:
        if ennemie.dead and ennemie.killFrame < 7:
            ennemie.killFrame += 1
        
def moveEnnemies(AIsprite):
    for sprite in AIsprite:
        sprite.move()

#Class for a CAR
class sprite:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.dead = 0
        
    def move(self, direction):
        if not self.dead:
            if direction == "left" and self.x > WIDTH-(WIDTH-30):
                self.x = self.x - (WIDTH-50)/10
            if direction == "right"and self.x < WIDTH - 30:
                self.x = self.x + (WIDTH-50)/10
            if direction == "up" and self.y > HEIGHT-(HEIGHT-50):
                self.y = self.y - (HEIGHT-65)/10
            if direction == "down"and self.y < HEIGHT - 50:
                self.y = self.y + (HEIGHT-65)/10
        
class mySprite(sprite):
    
    def __init__(self, x, y):
        super().__init__(x, y)
    
class AIsprite(sprite):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.just_killed = 1
        self.killFrame = 7
        