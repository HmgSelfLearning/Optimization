# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 15:55:20 2025

@author: hadis
"""

import pulp

model = pulp.LpProblem("maximize_profit", pulp.LpMaximize)

x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')

model += 30*x+40*y, "Total Profit"

model += 2*x+y <=100, "Labor Hours Constraint"
model += x+3*y <=80, "Material Units Constraint"

model.solve()

print(f"unit of product A: {x.varValue}")
print(f"unit of product B: {y.varValue}")
print(f"Total profit: ${pulp.value(model.objective)}")


