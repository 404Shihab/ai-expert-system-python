# ### Problem: Maximize f(x) = x<sup>2</sup> - 11x + 150 when x = 0 to 255

# Representation or ecoding solution:
# x can be represented using 8 bits binary number.

# # Step 1: Initialize Population

import random
def initPopulation(b=8, n =10): # n is the number of solutions, b is the length
    p = [random.choices([0,1],k = b) for i in range(n)] 
    return p

initPopulation(8,12)

# # Step 2: Reproduction or Parent Selection

# Fitness Calculation

def binToDecimal(binList):
  decValue = 0 # decimel value
  power = len(binList)
  for digit in binList: # binary to decimel
    decValue += digit*2**(power-1)
    power -= 1
  return decValue

def func(x):
  return x**2 - 11*x + 150

def getFitness(p): # p is the whole population
    f = [] # to store fitness values
    for sol in p:
        d = binToDecimal(sol)
        v = func(d)
        if v< 0: f.append(0)
        else: f.append(v) # fitness function
    return f

binToDecimal([1,0,0,1,0])

func(18)

population = initPopulation(8,6)
getFitness(population)

# calculate probability and select parents

import numpy as np
def select_parent(n, pop): # probability, parent selection
    # probability
    fitness = getFitness(pop)
    total_fitness = sum(fitness)
    prob = [f/total_fitness for f in fitness]
    cumSumProb = np.cumsum(prob)
    #print(cumSumProb)
    # parent selection
    parents = []
    for i in range(n):
        # roullete wheel, generate a random number
        r = random.random()
        #print(r)
        # check bin number of r        
        for j in range(len(cumSumProb)):
            if r <= cumSumProb[j] :#checking the bin
                #print(j)
                parents.append(pop[j])
                break
    return parents

population = initPopulation(8,10)
print(population)
parents = select_parent(4, population)
print(parents)

# # Step 3: Crossover

# define a method crossover (input is parents set)
def cross(p):
  num_cross = len(p)//2
  # print(num_cross)
  offsprings = []
  #  for loop to perform crossovers
  for i in range(num_cross):
   cp = random.choice(range(3,6))
   # print(cp)
   # perform crossover
   x,y = p[0],p[1]
   # modify the above line as the parents will be different for each crossover
   off1 = x[:cp] + y[cp:]
   offsprings.append(off1)

   # write code for off2

  return offsprings

off = cross(parents)
off

# # Step 4: Mutation

# Perform mutation with 3% probability
# def mutate(offsp, pr = 0.03):

# # Step 5: Select Survivor
# The selected survivors (solutions) will be added to population

# Select top 2 offspring based on fitness value and add them to population.

# define a method to select top offsprings (input offsprings, top)
def select_survivor(offsp):
  topOffsp = []
  f = getFitness(offsp)
  mInd = f.index(max(f))
  topOffsp.append(offsp[mInd])
  f.pop(mInd)
  #print(f)
  mInd = f.index(max(f))
  topOffsp.append(offsp[mInd])
  return topOffsp

select_survivor(off)

def best(p):
  f = getFitness(p)
  mInd = f.index(max(f))
  return p[mInd], max(f)

# # **Complete iteration**

# modify the below code to iterate the process for 3 generations
# in each generation show the best solution in population with fitness value
population = initPopulation(8,10)
print(best(population))
parents = select_parent(6, population)
offsprings = cross(parents)
# call mutation here
survivors = select_survivor(offsprings)
updatedPopulation = population + survivors
updatedPopulation