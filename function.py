import math
import numpy as np
import pandas as pd

def f(x): return (x**4) - (x) - 10
# pow(x,2)-(3*x)-4
def df(x): return (4*(x**3))-1

def ddf(x): return 12*(x**2)

def g(x): return (x+10)**(1/4)

def regresiveSustitution(Ab,n, indexes = 0):
    solutions = []
    Ab= np.array(Ab,float)
    for i in range(n,-1,-1):
        sum = 0
        for p in range(i+1,n+1):
            sum = sum + Ab[i][p] 
        xi = (Ab[i][n+1] - sum)/Ab[i][i] 
        if(not isinstance(indexes,int)):
            solutions.append('x%s = %s' %(indexes[i],xi))
        else:
            solutions.append('x%s = %s' %(i,xi))
    return solutions

def getMultipliers(Ab,nCol):
    col = Ab[:,nCol]
    f = lambda x: x/col[nCol]
    multipliers = f(col)
    multipliers = multipliers[nCol+1:]
    return multipliers

def rowOps(Ab,nCol,multipliers):
    col = Ab[:,nCol]
    pivot = np.tile(Ab[nCol,:],(col.size-nCol-1,1))
    mMatrix = (pivot.transpose()*multipliers).transpose()
    arr = np.arange(0,nCol+1)
    r = np.delete(Ab,arr,0) - mMatrix
    for val in reversed(arr):
        r = np.insert(r,0,[Ab[val,:]],0)
    return r
