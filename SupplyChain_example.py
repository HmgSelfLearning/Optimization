# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 12:24:24 2025

@author: hadis
"""

import gurobipy as gp
from gurobipy import GRB

model = gp.Model("SupplyChain")

factories = ['A', 'B', 'C']
distribution = [1,2,3,4]

C = {'A':100, 'B':150, 'C':200} #production capacity of each factory
P = {'A':5, 'B':4, 'C':6} #production fixed cost
D ={1:80, 2: 65, 3:70, 4:85} #demand of each distribution centerr 
S = {('A',1):2 , ('A',2):3, ('A',3):2.5 , ('A',4):3.5,
     ('B',1):2.5 , ('B',2):2, ('B',3):3 , ('B',4):2.5,
     ('C',1):3 , ('C',2):3.5, ('C',3):2 , ('C',4):2.5,
     } #Shiping cost of each production to each distribution center

x = model.addVars(factories, distribution, name="x", vtype = GRB.CONTINUOUS)
y = model.addVars(factories, name = "y", vtype = GRB.CONTINUOUS)

model.setObjective(gp.quicksum(P[i]*x[i,j] + S[i,j]* x[i,j] for i in factories for j in distribution), GRB.MINIMIZE)

model.addConstrs(y[i]<=C[i] for i in factories)
model.addConstrs(gp.quicksum(x[i,j] for i in factories) == D[j] for j in distribution)
#model.addConstrs(gp.quicksum(x[i,j] for j in distrribution) == C[i] for i in factories)
model.addConstrs(gp.quicksum(x[i,j] for j in distribution) == y[i] for i in factories)
model.addConstrs(x[i,j] >= 0 for i in factories for j in distribution)

model.optimize()


if model.status == GRB.OPTIMAL:
    print(f"Optimal objective is : {model.objVal}")
    for v in model.getVars():
        print(f"{v.VarName}: {v.x}")
            
    model.printAttr('x')
    model.printQuality()
    
else:
    print("No optimal solution found.")
        
    


 


