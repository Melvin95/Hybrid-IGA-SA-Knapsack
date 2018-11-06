import AnnealingFunctions
import random

class SimulatedAnnealing(object):
    def __init__(self,problem_size,max_iterations,temp_max,temp_change,KnapsackObj):
        self.ProblemSize = problem_size
        self.MaxIterations = max_iterations
        self.MaxTemp = temp_max
        self.temp_change = temp_change
        self.AF = AnnealingFunctions.AnnealingFunctions(KnapsackObj)

    def run_sa(self):
        current = self.AF.getRandomSolution()
        best = current
        temp = self.MaxTemp
        x = [0]
        y = [self.AF.getValue(best)]
        for i in range(self.MaxIterations):
            neigbourSolution = self.AF.getNeighbouringSolution(current)
            temp = self.AF.getTemperature(i,temp,self.temp_change)
            siCost = self.AF.getValue(neigbourSolution)
            sCost = self.AF.getValue(current)
            if  siCost <= sCost:
                current = neigbourSolution
                if siCost <= self.AF.getValue(best):
                    best = neigbourSolution
            elif self.AF.getMonteCarlo(sCost,siCost,temp) > random.uniform(0,1):
                current = neigbourSolution
                print("hello")
            x.append(i+1)
            y.append(-1*self.AF.getValue(current))
        return best,x,y
