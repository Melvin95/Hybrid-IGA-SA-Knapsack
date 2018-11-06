import math

class Knapsack(object):
    def __init__(self,weights,values,maxWeight):
        self.weights = weights
        self.values = values
        self.maxWeight = maxWeight

    def getProblemSize(self):
        return len(self.values)

    def sumWeights(self,indiviual):
        w = 0
        for i in range(len(indiviual)):
            if indiviual[i]==1:
                w += self.weights[i]
        return w

    def sumValues(self,indiviual):
        v = 0
        for i in range(len(indiviual)):
            if indiviual[i]==1:
                v += self.values[i]
        return v

    def fitness(self,indiviual):
        '''Very simple fitness function'''
        sumWeights = self.sumWeights(indiviual)
        penalty = 1
        if sumWeights>self.maxWeight:
            penalty = sumWeights+math.fabs(self.maxWeight-sumWeights)

        fitness = (self.sumValues(indiviual))-(penalty)
        return fitness

    def getValues(self):
        return self.values

    def getWeights(self):
        return self.weights
