import random
import math

class AnnealingFunctions(object):
    def __init__(self,obj):
        self.obj = obj

    def getRandomSolution(self):
        '''Returns bit-array of length prob_size'''
        individual = []
        for i in range(self.obj.getProblemSize()):
            individual.append(random.randint(0,1))
        return individual

    def getNeighbouringSolution(self,individual):
        sumWeights = self.obj.sumWeights(individual)
        #too full, remove a random item
        if self.obj.maxWeight<sumWeights:
            found = False
            while found==False:
                index = random.randint(0,self.obj.getProblemSize()-1)
                if individual[index]==1:
                    individual[index] = 0
                    found = True
                    return individual,index
        #too empty, add a random item
        else:
            found = False
            while found == False:
                index = random.randint(0,self.obj.getProblemSize()-1)
                if individual[index]==0:
                    individual[index]=1
                    found=True
                    return individual,index

    def getTemperature(self,i,temp,temp_change):
        if i==0:
            return temp
        else:
            return temp*temp_change

    def getMonteCarlo(self,current,si,temp):
        delta_cost = math.fabs(current - si)
        return math.exp(delta_cost/temp)

    def getValue(self,solution):
        return (-1)*self.obj.fitness(solution)
