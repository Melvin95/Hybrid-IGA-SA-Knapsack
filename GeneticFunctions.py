import random

'''
Standard GA functions wrapped
'''

class GeneticFunctions(object):
    def __init__(self,obj):
        '''obj: problem specific fitness function'''
        self.obj = obj

    def generateRandomIndividual(self,prob_size):
        '''Returns bit-array of length prob_size'''
        individual = []
        for i in range(prob_size):
            individual.append(random.randint(0,1))
        return individual

    def initializePopulation(self,pop_size,prob_size):
        '''Returns a population of pop_size with
           each individual a bit-array of length prob_size'''
        population = []
        for i in range(pop_size):
            population.append(self.generateRandomIndividual(prob_size))
        return population

    def evaluatePopulation(self,population):
        '''Returns evaluations of population '''
        evaluations = []
        for indiviual in population:
            evaluations.append(self.obj.fitness(indiviual))
        return evaluations

    def evaluateIndividual(self,indiviual):
        return self.obj.fitness(indiviual)

    def getBest(self,evaluations):
        '''returns index of best solution in population'''
        bestindex = 0
        bestEval = evaluations[0]
        for i in range(1,len(evaluations)):
            if evaluations[i]>bestEval:
                bestindex = i
                bestEval = evaluations[i]
        return bestindex

    def getParents(self,population,evaluations,k):
        '''Return parents using K-Tournament Selection'''
        parents = []
        for i in range(len(population)):
            candidates = []
            temp = []
            #Select k indiviuals
            for j in range(k):
                index = random.randint(0,len(population)-1)
                candidates.append(population[index])
                temp.append(evaluations[index])
            #Add best from sub-population of k-individuals
            parents.append(candidates[self.getBest(temp)])
        return parents

    def crossover(self,parent1,parent2):
        '''One-point Cross Over Operator returns two children'''
        point = random.randint(0,len(parent1)-1)
        child1 = []
        child2 = []
        for i in range(len(parent1)):
            if i<point:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])
        return child1,child2

    def mutate(self,indiviual):
        '''Random mutation of gene, Return mutated indiviual'''
        point1 = random.randint(0,len(indiviual)-1)
        point2 = random.randint(0,len(indiviual)-1)
        temp = indiviual[point1]
        indiviual[point1] = indiviual[point2]
        indiviual[point2] = temp
        return indiviual
