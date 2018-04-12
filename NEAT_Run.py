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
def eval_genomes(genomes, config):
    i = 0
    global GENERATION, MAX_FITNESS, BEST_GENOME, highScore

    GENERATION += 1
    #Instantiate game
    game = Game()
    #Iterate through each genome seperately (for now, might change in future)
    for genome_id, genome in genomes:
        #Run game and return fitness
        genome.fitness = game.game(genome, config, 1)
        #Print Results in Console
        print("Gen:" + str(GENERATION) + " Gnm:" + str(i) + " MyFit:" + str(round(genome.fitness)) + " TopFit:" + str(round(MAX_FITNESS)) + " TopSCR:"+str(highScore))
        if genome.fitness >= MAX_FITNESS:
            MAX_FITNESS = genome.fitness
            BEST_GENOME = genome
        if(myGlobals.SCORE > highScore):
            highScore = myGlobals.SCORE
        myGlobals.SCORE = 0
        i+=1

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
