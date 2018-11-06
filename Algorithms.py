import random
import AnnealingFunctions
import GeneticFunctions
import time

class Algorithm:
    def __init__(self):
        self.name = 'Algorithm'
    def run(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def getName(self):
        return self.name

class SimulatedAnnealing(Algorithm):
    def __init__(self,max_iterations,temp_max,temp_change,KnapsackObj):
        self.ProblemSize = KnapsackObj.getProblemSize()
        self.MaxIterations = max_iterations
        self.MaxTemp = temp_max
        self.temp_change = temp_change
        self.AF = AnnealingFunctions.AnnealingFunctions(KnapsackObj)
        self.name = 'Simulated Annealing'

    def run(self):
        start_time = int(round(time.time() * 1000))
        current = self.AF.getRandomSolution()
        best = current
        temp = self.MaxTemp
        x = [0]
        y = [(-1)*self.AF.getValue(best)]
        operations = self.ProblemSize #initially generating a random solution
        for i in range(self.MaxIterations):
            neigbourSolution,temp = self.AF.getNeighbouringSolution(current)
            operations += temp
            temp = self.AF.getTemperature(i,temp,self.temp_change)
            siCost = self.AF.getValue(neigbourSolution)
            sCost = self.AF.getValue(current)
            operations += self.ProblemSize*2 #two problems & fitness function depends on problem size
            if  siCost <= sCost:
                current = neigbourSolution
                if siCost <= self.AF.getValue(best):
                    best = neigbourSolution
                operations += self.ProblemSize
            elif self.AF.getMonteCarlo(sCost,siCost,temp) > random.uniform(0,1):
                current = neigbourSolution
            x.append(i+1)
            y.append((-1)*self.AF.getValue(current)) #for graph, don't add to operations
        end_time = int(round(time.time() * 1000))
        return best,x,y,operations,end_time-start_time

class GeneticAlgorithm(Algorithm):
    def __init__(self,pop_size=100,pcross=0.6,pmutate=0.3,k=20,MaxIterations=500,KnapsackObj=None):
        self.PopulationSize = pop_size
        self.ProblemSize = KnapsackObj.getProblemSize()
        self.Pcrossover = pcross
        self.Pmutation = pmutate
        self.k = k  #for k-Tournament selection
        self.MaxIterations = MaxIterations

        if self.PopulationSize%2!=0:
            self.PopulationSize = self.PopulationSize-1

        self.GF = GeneticFunctions.GeneticFunctions(KnapsackObj)

        self.name = 'Genetic Algorithm'

    def run(self):
        '''GA'''
        start_time = int(round(time.time() * 1000))
        #Initialize population
        population = self.GF.initializePopulation(self.PopulationSize,self.ProblemSize)
        evaluations = self.GF.evaluatePopulation(population)
        bestever = population[self.GF.getBest(evaluations)]
        currentbest = bestever

        #stuff for plotting graph
        x = [0] #iteration
        y = [self.GF.evaluateIndividual(currentbest)] #fitness values

        #Need to initialize population,evaluate population and then find best fit
        operations = ((self.PopulationSize*self.ProblemSize)*2)+self.PopulationSize

        #Genetic Algorithm
        for i in range(self.MaxIterations):
            #selection
            parents = self.GF.getParents(population,evaluations,self.k)
            operations += self.PopulationSize
            children = []
            for i in range(0,len(parents),2):
                parent1 = parents[i]
                parent2 = parents[i+1]
                child1,child2 = parent1,parent2
                #crossover
                if random.uniform(0,1)<self.Pcrossover:
                    child1,child2 = self.GF.crossover(parent1,parent2)
                    operations += self.ProblemSize
                #mutate
                if random.uniform(0,1)<self.Pmutation:
                    child1 = self.GF.mutate(child1)
                    operations += 2
                if random.uniform(0,1)<self.Pmutation:
                    child2 = self.GF.mutate(child2)
                    operations += 2

                children.append(child1)
                children.append(child2)

            #Replace population with next children
            evaluations = self.GF.evaluatePopulation(children)
            operations += (self.PopulationSize*self.ProblemSize)
            population = children
            #Track change in fittest indiviual
            bestindex = self.GF.getBest(evaluations)
            operations += self.ProblemSize
            currentbest = population[bestindex]
            if evaluations[bestindex]>self.GF.evaluateIndividual(bestever):
                bestever = currentbest
            operations += self.ProblemSize
            x.append(i+1)
            y.append(evaluations[bestindex])
        end_time = int(round(time.time() * 1000))
        return bestever,x,y,operations,end_time-start_time

class GeneticAnnealing(Algorithm):
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

        self.name = "Hybrid IGA-SA"

    def run(self):
        start_time = int(round(time.time() * 1000))
        #Initialize population
        population = self.GA.initializePopulation(self.population_size,self.problem_size)
        evaluations = self.GA.evaluatePopulation(population)
        bestever = population[self.GA.getBest(evaluations)]
        currentbest = bestever
        x = [0]
        y = [self.GA.evaluateIndividual(currentbest)]
        temp = self.temp_max
        #Need to initialize population,evaluate population and then find best fit
        operations = ((self.population_size*self.problem_size)*2)+self.population_size
        for i in range(self.GA_iterations):
            parents = self.GA.getParents(population,evaluations,self.k)
            operations += self.problem_size
            children = []
            for p in range(0,len(parents),2):
                parent1 = parents[p]
                parent2 = parents[p+1]
                child1,child2 = parent1,parent2
                #crossover
                if random.uniform(0,1)<self.pcross:
                    child1,child2 = self.GA.crossover(parent1,parent2)
                    operations += self.problem_size
                #mutate
                if random.uniform(0,1)<self.pmutate:
                    child1 = self.GA.mutate(child1)
                    operations += 2
                if random.uniform(0,1)<self.pmutate:
                    child2 = self.GA.mutate(child2)
                    operations += 2

                children.append(child1)
                children.append(child2)

            #Replace population with next children
            evaluations = self.GA.evaluatePopulation(children)
            population = children
            operations += (self.population_size*self.problem_size)

            #Send fittest indiviual to SA
            bestindex = self.GA.getBest(evaluations)
            currentbest = population[bestindex]
            operations += self.problem_size

            for j in range(self.SA_iterations):
                neigbourSolution,temp = self.SA.getNeighbouringSolution(currentbest)
                operations += temp
                temp = self.SA.getTemperature(i,temp,self.temp_change)
                siCost = self.SA.getValue(neigbourSolution)
                sCost = self.SA.getValue(currentbest)
                operations += self.problem_size*2
                if  siCost <= sCost:
                    currentbest = neigbourSolution
                    if siCost <= self.SA.getValue(bestever):
                        bestever = neigbourSolution
                    operations + self.problem_size
                elif self.SA.getMonteCarlo(sCost,siCost,temp) > random.uniform(0,1):
                    currentbest = neigbourSolution

            currentbestEval = self.GA.evaluateIndividual(currentbest)
            #if evaluations[bestindex]<currentbestEval:
            population[bestindex] = currentbest
            evaluations[bestindex] = currentbestEval
            x.append(i+1)
            y.append(evaluations[bestindex])

        end_time = int(round(time.time() * 1000))
        return bestever,x,y,operations,end_time-start_time
