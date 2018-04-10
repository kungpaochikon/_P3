import neat
import sys
import random
import pickle

GENERATION = 0
MAX_FITNESS = 0
BEST_GENOME = 0

def game(genome, config):

    network = neat.nn.FeedForwardNetwork.create(genome,config)

    numPassed = 0

    while True:
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        input = (num1,num2)
        fitness = numPassed
        output = network.activate(input)
        print("Number1: "+str(num1))
        print("Number2: "+str(num2))
        print("AVG: "+str((num1+num2)/2))
        print("Output: "+str(output[0]*10))
        if(abs(output[0]*10 - (num1+num2)/2)>3 or numPassed>500):
            print("DONE!!!!!!!!!!!")
            return fitness
        numPassed+=1
        

    

def eval_genomes(genomes, config):
    i = 0
    global SCORE
    global GENERATION, MAX_FITNESS, BEST_GENOME

    GENERATION += 1
    for genome_id, genome in genomes:
        
        genome.fitness = game(genome, config)
        print("Gen : %d Genome # : %d  Fitness : %f Max Fitness : %f"%(GENERATION,i,genome.fitness, MAX_FITNESS))
        if genome.fitness >= MAX_FITNESS:
            MAX_FITNESS = genome.fitness
            BEST_GENOME = genome
        SCORE = 0
        i+=1

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'conf')

pop = neat.Population(config)
stats = neat.StatisticsReporter()
pop.add_reporter(stats)

winner = pop.run(eval_genomes, 80)

print(winner)

outputDir = 'bestGenomes'
outputFile = open(outputDir+'\_'+str(int(MAX_FITNESS))+'.p','wb' )
pickle.dump(winner, outputFile)
outputFile.close();

sys.exit();
