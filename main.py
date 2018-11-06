import utilities as ut
import KnapSack as KS
import numpy as np
import Algorithms
import os

class Main(object):
    def __init__(self,dataset="./TestDataset/f1_l-d_kp_10_269",num_iterations=1,algorithm=0,
                population_size=100,Pcross=0.8,Pmutate=0.2,k=20,GA_iterations=100,
                SA_iterations=2000,MaxTemp=200,TempChange=0.80,
                HybridGAIterations=150,HybridSAIterations=150):

        self.dataset = dataset
        self.num_iterations = num_iterations

        self.filename_w_ext = os.path.basename(dataset)
        #try:
        self.optimal_value = ut.getOptimalValue(self.filename_w_ext)
        #except:
        #self.optimal_value = 0

        #get file into array
        #self.arr = ut.readfile("./TestDataset/"+self.dataset)
        self.arr = ut.readfile(self.dataset)

        self.n_items = self.arr[0][0] #first line first element
        self.max_weight = self.arr[0][1] #first line second element

        self.population_size = population_size
        if self.population_size%2!=0:
            self.population_size += 1
        self.Pcross = Pcross
        self.Pmutate = Pmutate
        self.k = k
        self.GA_iterations = GA_iterations

        self.SA_iterations = SA_iterations
        self.MaxTemp = MaxTemp
        self.TempChange = TempChange

        self.HybridGAIterations = HybridGAIterations
        self.HybridSAIterations = HybridSAIterations

        #split into weights and values
        self.weights = []
        self.values = []
        for pair in self.arr[1:]:
            self.values.append(pair[0])
            self.weights.append(pair[1])

        #Initialize problem
        self.myKnapSack = KS.Knapsack(weights=self.weights,values=self.values,maxWeight=self.max_weight)

        #Initialize an algorithm
        self.algorithm = None
        if algorithm==1:
            self.algorithm = Algorithms.GeneticAlgorithm(pop_size=self.population_size,KnapsackObj=self.myKnapSack,pcross=self.Pcross,pmutate=self.Pmutate,MaxIterations=self.GA_iterations,k=self.k)
        elif algorithm==2:
            self.algorithm = Algorithms.SimulatedAnnealing(max_iterations=self.SA_iterations,temp_max=self.MaxTemp,temp_change=self.TempChange,KnapsackObj=self.myKnapSack)
        else:
            self.algorithm = Algorithms.GeneticAnnealing(population_size=self.population_size,problem_size=self.n_items,pcross=self.Pcross,pmutate=self.Pmutate,temp_max=self.MaxTemp,temp_change=self.TempChange,GA_iterations=self.HybridGAIterations,SA_iterations=self.HybridSAIterations,k=self.k,KnapsackObj=self.myKnapSack)

    def Run(self):
        allX,allY = [],[] #iterations,fitness
        v,w = [],[] #value,weight
        o = []
        t = []
        solutions = []
        for i in range(self.num_iterations):
            best,x,y,operations,runt = self.algorithm.run()
            allX.append(x)
            allY.append(y)
            o.append(operations)
            t.append(runt)
            v.append(self.myKnapSack.sumValues(best))
            w.append(self.myKnapSack.sumWeights(best))
            solutions.append(best)

        #Plot
        save_name = self.algorithm.getName()+"_"+str(self.num_iterations)+"_"+self.filename_w_ext
        ut.plotgraph(allX,allY,self.algorithm.getName()+": Fitness over "+str(self.num_iterations)+" iteration(s)",save_name)
        ut.scattergraph(v,w,self.optimal_value,self.algorithm.getName()+": Value-Weigth Solution Pairs for "+str(self.num_iterations)+" iteration(s)",save_name)

        '''saving results to csv'''
        data = list()
        best_index = np.argmax(v)
        #data.append(['Algorithm','Dataset','Iteration','Number Of Items','Best Value','Optimal Value','Shortfall','Operations','Time (Milli)'])
        data.append([self.algorithm.getName(),self.filename_w_ext,self.num_iterations,self.n_items,v[best_index],self.optimal_value,self.optimal_value-v[best_index],o[best_index],t[best_index]])
        ut.write_file(data,"./"+self.algorithm.getName()+"_Results.csv")
        return v[best_index],w[best_index],solutions[best_index],self.max_weight,self.myKnapSack


'''MAIN ENTRANCE HERE'''
filenames = ut.getListofFiles('./TestDataset')
for f in filenames:
    try:
        print('Processing data set '+f)
        m = Main(dataset='./TestDataset/'+f,num_iterations=10,algorithm=0)
        m.Run()
        print('Done processing')
    except Exception as e:
        print("Something went wrong with "+f)
        print(e)
        pass
