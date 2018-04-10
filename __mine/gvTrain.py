#Inspiration/Learning From:
#https://github.com/llSourcell/neuroevolution-for-flappy-birds

import pygame
from pygame.locals import *
import sys
import random
from player import Player
from obstacle import Obstacle

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
    #Player Character
    player = Player(PANEL)
    #Obstacles
    obsU1 = Obstacle(PANEL,512,256,False)
    obsL1 = Obstacle(PANEL,512,256,True)
    obsU2 = Obstacle(PANEL,512+200,160,False)
    obsL2 = Obstacle(PANEL,512+200,160,True)
    #Create List of Obstacles for easy handling
    obsList = []
    obsList.append(obsU1)
    obsList.append(obsL1)
    obsList.append(obsU2)
    obsList.append(obsL2)
    #Create Group of Sprites for Collision Detection
    obsGroup = pygame.sprite.Group()
    for obs in obsList:
        obsGroup.add(obs)
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
        for obs in obsList:
            obs.step()
            if(obs.x < 0 - obs.w):
                obs.x = obs.x + WIDTH * 1.5
        #Check Collision
        collision = pygame.sprite.spritecollideany(player,obsGroup)
        if(collision!=None):
            print("GAME OVER")
            close()
        
        pygame.display.update()
        CLOCK.tick(FPS)    

def close():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

game()
close()
