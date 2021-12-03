import pygame

#frame rate
FRAME_RATE = 7

#screen size
WIDTH = 600
HEIGHT = 600

#player'sprites
FRONT1 = pygame.image.load(".\\sprites\\doom_guy\\front1.png")
FRONT0 = pygame.image.load(".\\sprites\\doom_guy\\front0.png")
BACK1 = pygame.image.load(".\\sprites\\doom_guy\\back1.png")
BACK0 = pygame.image.load(".\\sprites\\doom_guy\\back0.png")
LEFT1 = pygame.image.load(".\\sprites\\doom_guy\\left1.png")
LEFT0 = pygame.image.load(".\\sprites\\doom_guy\\left0.png")
RIGHT1 = pygame.image.load(".\\sprites\\doom_guy\\right1.png")
RIGHT0 = pygame.image.load(".\\sprites\\doom_guy\\right0.png")

#AI s'sprites
STILL00 = pygame.image.load(".\\sprites\\imps\\still00.png")
STILL01 = pygame.image.load(".\\sprites\\imps\\still01.png")
STILL10 = pygame.image.load(".\\sprites\\imps\\still10.png")
STILL11 = pygame.image.load(".\\sprites\\imps\\still11.png")
STILL20 = pygame.image.load(".\\sprites\\imps\\still20.png")
STILL21 = pygame.image.load(".\\sprites\\imps\\still21.png")

FRONTI1 = pygame.image.load(".\\sprites\\imps\\front1.png")
FRONTI0 = pygame.image.load(".\\sprites\\imps\\front0.png")
BACKI1 = pygame.image.load(".\\sprites\\imps\\back1.png")
BACKI0 = pygame.image.load(".\\sprites\\imps\\back0.png")
LEFTI1 = pygame.image.load(".\\sprites\\imps\\left1.png")
LEFTI0 = pygame.image.load(".\\sprites\\imps\\left0.png")
RIGHTI1 = pygame.image.load(".\\sprites\\imps\\right1.png")
RIGHTI0 = pygame.image.load(".\\sprites\\imps\\right0.png")

#death
DEAD = pygame.image.load(".\\sprites\\imps\\death7.png")

MAX_ENNEMIES = 10