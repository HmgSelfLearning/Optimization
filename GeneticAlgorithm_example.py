# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:10:01 2024

@author: hmoazami
"""
"""
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

nVars = 8

def f(x):
    pen=0
    if not x[0]+x[1]==1: pen=np.inf
    if not x[5]+x[6]+x[7]==1: pen=np.inf
    if not x[2]+x[3]==x[0]: pen=np.inf
    if not x[4]==x[1]: pen=np.inf
    if not x[5]==x[2]: pen=np.inf
    if not x[6]==x[3]: pen=np.inf
    if not x[7]==x[4]: pen=np.inf
    return 220*x[0]+1500*x[1]+650*x[2]+900*x[3]+500*x[4]+500*x[5]+400*x[6]+400*x[7] +pen


varbounds = np.array([[0,1]]*nVars)

vartype = np.array([['int']]*nVars)

model = ga(function=f, dimension=nVars, variable_type_mixed=vartype, variable_boundaries=varbounds)

model.run()
"""

import pandas as pd, numpy as np
from geneticalgorithm import geneticalgorithm as ga
 
#inputs
nodes = pd.read_excel('route_inputs.xlsx', sheet_name='nodes')
paths = pd.read_excel('route_inputs.xlsx', sheet_name='paths')
nVars = len(paths)
 
#fitness function
def f(x):
    pen = 0
    
    #constraint sum(x) == 1 (origin)
    node_origin = int(nodes.node[nodes.description=='origin'])
    if sum([x[p] for p in paths.index[paths.node_from==node_origin]]) != 1:
        pen += 1000000 * np.abs(sum([x[p] for p in paths.index[paths.node_from==node_origin]]) - 1)
    
    #constraint sum(x) == 1 (destination)
    node_destination = int(nodes.node[nodes.description=='destination'])
    if sum([x[p] for p in paths.index[paths.node_to==node_destination]]) != 1:
        pen += 1000000 * np.abs(sum([x[p] for p in paths.index[paths.node_to==node_destination]]) - 1)
    
    #constraint sum(x, in) == sum(x, out)
    for node in nodes.node[nodes.description=='middle point']:
        sum_in = sum([x[p] for p in paths.index[paths.node_to==node]])
        sum_out = sum([x[p] for p in paths.index[paths.node_from==node]])
        if sum_in != sum_out:
            pen += 1000000 * np.abs(sum_in - sum_out)
 
    #objective function and return
    objFun = sum([x[p] * paths.distance[p] for p in paths.index])
    return objFun + pen
 
#bounds and var type
varbounds = np.array([[0,1]]*nVars)
vartype = np.array([['int']]*nVars)
 
#GA parameters
algorithm_param = {'max_num_iteration': 500,\
                   'population_size':100,\
                   'mutation_probability':0.30,\
                   'elit_ratio': 0.10,\
                   'crossover_probability': 0.50,\
                   'parents_portion': 0.30,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':100}
 
#Solve
model = ga(function=f,
           dimension=nVars,
           variable_type_mixed=vartype,
           variable_boundaries=varbounds,
           algorithm_parameters=algorithm_param)
model.run()
 
#print
x = model.best_variable
objFun = model.best_function
paths['activated'] = 0
for p in paths.index:
    paths.activated[p] = x[p]
 
print('\n\nAll Paths:')
print(paths)
 
print('\nSelected Paths:')
print(paths[paths.activated==1])
 
print('\nTotal path:', objFun)