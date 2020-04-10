import numpy as np

def regresiveSustitution(Ab,n, indexes = 0):
    solutions = []
    Ab= np.array(Ab,float)
    for i in range(n,-1,-1):
        sum = 0
        for p in range(i+1,n+1):
            sum = sum + Ab[i][p] * solutions[n-p][1]
        xi = (Ab[i][n+1] - sum)/Ab[i][i] 
        if(not isinstance(indexes,int)):
            solutions.append(['x%s =' %(indexes[i]),xi])
        else:
            solutions.append(['x%s =' %(i),xi])
    return reversed(solutions)

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

def swapRows(A,nCol,nInd,indexes):
    A[[nCol, nInd+nCol]] = A[[nInd+nCol , nCol]]
    indexes[nCol], indexes[nInd+nCol] = indexes[nInd+nCol], indexes[nCol] 
    return A,indexes

def isSquared(A):
    return all(len(row) == len(A) for row in A)
