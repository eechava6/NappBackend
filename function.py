import math
import numpy as np

def f(x): return (x**4) - (x) - 10
# pow(x,2)-(3*x)-4
def df(x): return (4*(x**3))-1

def ddf(x): return 12*(x**2)

def g(x): return (x+10)**(1/4)

def regresiveSustitution(Ab,n):
    solutions = []
    Ab= np.array(Ab,float)
    for i in range(n,-1,-1):
        sum = 0
        for p in range(i+1,n+1):
            sum = sum + Ab[i][p] 
        xi = (Ab[i][n+1] - sum)/Ab[i][i] 
        solutions.append('x%s = %s' %(i,xi))
    return solutions

def getArr(n):
    arr = []
    for val in range(0,n+1):
        arr.append(val)
    return arr

def rowOps(Ab,nCol):
    
    col = Ab[:,nCol]
    f = lambda x: x/col[nCol]
    multipliers = f(col)
    multipliers = multipliers[nCol+1:]
    #Verify if worth doing the op (Multipliers different to zero)
    if(np.count_nonzero(multipliers) == 0):
        return 0
    pivot = np.tile(Ab[nCol,:],(col.size-nCol-1,1))
    mMatrix = (pivot.transpose()*multipliers).transpose()
    arr = getArr(nCol)
    r = np.delete(Ab,arr,0) - mMatrix
    for val in reversed(arr):
        r = np.insert(r,0,[Ab[val,:]],0)
    return r
