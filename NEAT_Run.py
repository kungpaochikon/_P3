import neat
import sys
import random
import pickle
from gvGame import Game
import myGlobals

GENERATION = 0
MAX_FITNESS = 0
BEST_GENOME = 0
myGlobals.SCORE = 0
highScore = 0
#Load Neat Config
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,'config')
#Load Specific File
genomeFile = 'bestGenomes/_871.p'
genome = pickle.load(open(genomeFile,'rb'))

game = Game()
for i in range(100):
    game.game(genome, config,1)
    myGlobals.SCORE = 0

game.close()
sys.exit();
