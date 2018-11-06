'''Some useful functions'''
import matplotlib.pyplot as plt
import csv
from os import listdir
from os.path import isfile, join
import os

def readfile(filename):
    '''read file into array of shape (n,2)'''
    arr = []
    try:
        f = open(filename).readlines()
        for line in f:
            split_string = line.split()
            arr.append([int(split_string[0]),int(split_string[1])])
    except Exception as e:
        print(e)
        print('here')
    return arr

def plotgraph(x,y,name,save_name):
    for i in range(len(x)):
        plt.plot(x[i],y[i])
    plt.xlabel('Iterations')
    plt.ylabel('Fitness Value')
    plt.title(name)
    #plt.show()
    plt.savefig('./Plots/FitnessVIterations_'+save_name+'.pdf')
    plt.gcf().clear()

def scattergraph(x,y,optx,name,save_name):
    for i in range(len(x)):
        if x[i]==optx:
            plt.scatter(x[i],y[i],color='green',label='Approximation=Optimal')
        else:
            plt.scatter(x[i],y[i],color='red',label='Approximation')
    plt.axvline(x=optx,color='blue',label='Optimal Value',linestyle='-')
    plt.xlabel('Profit')
    plt.ylabel('Weights')
    plt.title(name)
    plt.legend(loc='best')
    #plt.show()
    plt.savefig('./Plots/Scatter_'+save_name+'.pdf')
    plt.gcf().clear()

def write_file(data,path):
    with open(path,"a") as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerows(data)

def read_csv(filename):
    with open(filename,'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

def getOptimalValue(dataset):
    '''returns optimal solution for given dataset'''
    value = 0
    try:
        f = open("./OptimalSolution/"+dataset).readlines()[0]
        value = int(f.split()[0])
    except Exception as e:
        print(e)
    return value

def getListofFiles(directory):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return files
