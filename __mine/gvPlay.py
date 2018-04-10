#Inspiration/Learning From:
#https://github.com/llSourcell/neuroevolution-for-flappy-birds

import pygame
from pygame.locals import *
import sys
import random
from player import Player

FPS = 60
WIDTH = 288
HEIGHT = 512
running = True
BACKGROUND = pygame.image.load("bg.png")

def game():
    pygame.init()
    CLOCK = pygame.time.Clock()
    PANEL = pygame.display.set_mode((WIDTH,HEIGHT))
    global SCORE
    player = Player(PANEL)
    while running:
        PANEL.blit(BACKGROUND,(0,0))
        #Get Inputs
        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                #Player Jump
                if(event.key == K_SPACE):
                    player.jump()
                #Close Game With Escape Key
                if(event.key == K_ESCAPE):
                    close()
        player.step()
        pygame.display.update()
        CLOCK.tick(FPS)    

def close():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

game()
close()
