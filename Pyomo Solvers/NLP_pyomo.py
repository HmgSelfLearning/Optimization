# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:15:52 2024

@author: hadis
"""

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(initialize=0, bounds=(-5,5))
model.y = pyo.Var(initialize=0, bounds=(-5,5))
x = model.x
y = model.y


model.obj = pyo.Objective(expr= cos(x+1)+ cos(x)*cos(y), sense=maximize)

#pt = SolverFactory('glpk')
opt = SolverFactory('ipopt', executable='C:\\ipopt\\bin\\ipopt.exe')
opt.solve(model)
opt.options['tol']=1e-6

model.pprint()

x_value = pyo.value(x)
y_value = pyo.value(y)

print('x=',x_value)
print('y=',y_value)