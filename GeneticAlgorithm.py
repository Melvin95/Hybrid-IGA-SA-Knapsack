'''
GA Implementation
'''
import GeneticFunctions
import random

class GeneticAlgorithm(object):
    def __init__(self,pop_size=100,problem_size=None,pcross=0.6,pmutate=0.3,k=20,MaxIterations=500,KnapsackObj=None):
        self.PopulationSize = pop_size
        self.ProblemSize = problem_size
        self.Pcrossover = pcross
        self.Pmutation = pmutate
        self.k = k  #for k-Tournament selection
        self.MaxIterations = MaxIterations

        if self.PopulationSize%2!=0:
            self.PopulationSize = self.PopulationSize-1

        self.GF = GeneticFunctions.GeneticFunctions(KnapsackObj)

    def run_ga(self):
        '''GA'''
        #Initialize population
        population = self.GF.initializePopulation(self.PopulationSize,self.ProblemSize)
        evaluations = self.GF.evaluatePopulation(population)
        bestever = population[self.GF.getBest(evaluations)]
        currentbest = bestever

        #stuff for plotting graph
        x = [0] #iteration
        y = [self.GF.evaluateIndividual(currentbest)] #fitness values

        #Genetic Algorithm
        for i in range(self.MaxIterations):

            #selection
            parents = self.GF.getParents(population,evaluations,self.k)
            children = []
            for i in range(0,len(parents),2):
                parent1 = parents[i]
                parent2 = parents[i+1]
                child1,child2 = parent1,parent2
                #crossover
                if random.uniform(0,1)<self.Pcrossover:
                    child1,child2 = self.GF.crossover(parent1,parent2)
                #mutate
                if random.uniform(0,1)<self.Pmutation:
                    child1 = self.GF.mutate(child1)
                if random.uniform(0,1)<self.Pmutation:
                    child2 = self.GF.mutate(child2)

                children.append(child1)
                children.append(child2)

            #Replace population with next children
            evaluations = self.GF.evaluatePopulation(children)
            population = children
            #Track change in fittest indiviual
            bestindex = self.GF.getBest(evaluations)
            currentbest = population[bestindex]
            if evaluations[bestindex]>self.GF.evaluateIndividual(bestever):
                bestever = currentbest
            x.append(i+1)
            y.append(evaluations[bestindex])

        return bestever,x,y
