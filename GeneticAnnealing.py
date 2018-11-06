import GeneticFunctions
import AnnealingFunctions
import random

class GeneticAnnealing(object):
    def __init__(self,population_size,problem_size,pcross,pmutate,temp_max,temp_change,GA_iterations,SA_iterations,k,KnapsackObj):
        self.population_size = population_size
        self.problem_size = problem_size
        self.pcross = pcross
        self.pmutate = pmutate
        self.temp_max = temp_max
        self.temp_change = temp_change
        self.GA_iterations = GA_iterations
        self.SA_iterations = SA_iterations
        self.k = k
        self.GA = GeneticFunctions.GeneticFunctions(KnapsackObj)
        self.SA = AnnealingFunctions.AnnealingFunctions(KnapsackObj)

        if self.population_size%2!=0:
            self.population_size += 1

    def run_igsa(self):
        #Initialize population
        population = self.GA.initializePopulation(self.population_size,self.problem_size)
        evaluations = self.GA.evaluatePopulation(population)
        bestever = population[self.GA.getBest(evaluations)]
        currentbest = bestever
        x = [0]
        y = [self.GA.evaluateIndividual(currentbest)]
        temp = self.temp_max
        for i in range(self.GA_iterations):
            parents = self.GA.getParents(population,evaluations,self.k)
            children = []
            for p in range(0,len(parents),2):
                parent1 = parents[p]
                parent2 = parents[p+1]
                child1,child2 = parent1,parent2
                #crossover
                if random.uniform(0,1)<self.pcross:
                    child1,child2 = self.GA.crossover(parent1,parent2)
                #mutate
                if random.uniform(0,1)<self.pmutate:
                    child1 = self.GA.mutate(child1)
                if random.uniform(0,1)<self.pmutate:
                    child2 = self.GA.mutate(child2)

                children.append(child1)
                children.append(child2)

            #Replace population with next children
            evaluations = self.GA.evaluatePopulation(children)
            population = children

            #Send fittest indiviual to SA
            bestindex = self.GA.getBest(evaluations)
            currentbest = population[bestindex]

            for j in range(self.SA_iterations):
                neigbourSolution = self.SA.getNeighbouringSolution(currentbest)
                temp = self.SA.getTemperature(i,temp,self.temp_change)
                siCost = self.SA.getValue(neigbourSolution)
                sCost = self.SA.getValue(currentbest)
                if  siCost <= sCost:
                    currentbest = neigbourSolution
                    if siCost <= self.SA.getValue(bestever):
                        bestever = neigbourSolution
                elif self.SA.getMonteCarlo(sCost,siCost,temp) > random.uniform(0,1):
                    currentbest = neigbourSolution

            population[bestindex] = currentbest
            x.append(i+1)
            y.append(self.GA.evaluateIndividual(population[bestindex]))

        return bestever,x,y
