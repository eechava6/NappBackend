import numpy as np
import pandas as pd
from decimal import *

def regresiveSustitution(Ab,n, indexes = 0):
    solutions = []
    Ab= np.array(Ab,float)
    for i in range(n,-1,-1):
        sum = 0
        for p in range(i+1,n+1):
            sum = sum + Ab[i][p] * solutions[n-p][1]
        xi = (Ab[i][n+1] - sum)/Ab[i][i] 
        if(not isinstance(indexes,int)):
            solutions.append(['x%s' %(indexes[i]),xi])
        else:
            solutions.append(['x%s' %(i),xi])
    return solutions[::-1]

def customRegresiveSustitution(Ab,n, indexes = 0):
    solutions = []
    Ab= np.array(Ab,float)
    for i in range(n,-1,-1):
        sum = 0
        for p in range(i+1,n+1):
            sum = sum + Ab[i][p] * solutions[n-p][1]
        xi = (Ab[i][n+1] - sum)/Ab[i][i]
        if(not isinstance(indexes,int)):
            solutions.append([(indexes[i]),xi])
        else:
            solutions.append([i,xi])
    return solutions[::-1]

def regresiveSustitutions(Ab,n, indexes = 0):
    solutions = []
    Ab= np.array(Ab,float)
    for i in range(n,-1,-1):
        sum = 0
        for p in range(i+1,n+1):
            sum = sum + Ab[i][p] * solutions[n-p][1]
        xi = (Ab[i][n+1] - sum)/Ab[i][i] 
        if(not isinstance(indexes,int)):
            solutions.append(['x%s' %(indexes[i]),xi])
        else:
            solutions.append(['x%s' %(i),xi])
    return solutions

def progressiveSustitution(Ab, n, indexes = 0):
    solutions = []
    Ab= np.array(Ab,float)
    for i in range(0,n):
        sum = 0
        for p in range(0,i):
            sum = sum + Ab[i][p] * solutions[p]
        xi = (Ab[i][n] - sum)/Ab[i][i]
        if(not isinstance(indexes,int)):
            solutions.append(xi)
        else:
            solutions.append(xi)
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
    r = np.round(r,14)
    return r

def swapRows(A,nCol,nInd,indexes, index = True):
    A[[nCol, nInd+nCol]] = A[[nInd+nCol , nCol]]
    if(index):
        pass
        #indexes[nCol], indexes[nInd+nCol] = indexes[nInd+nCol], indexes[nCol]
    return A,indexes

def swapRows2(A,nCol,nInd,indexes, index = True):
    A[[nCol, nInd+nCol]] = A[[nInd+nCol , nCol]]
    if(index):
        indexes[nCol], indexes[nInd+nCol] = indexes[nInd+nCol], indexes[nCol]
    return A,indexes

def swapCols(A,Col1,Col2):
    for k in range(len(A)):
        A[k][Col1], A[k][Col2+Col1] = A[k][Col2+Col1], A[k][Col1]
    return A

def swapRowsSpecial(A,nCol,nInd):
    qty = min(nCol,nInd)
    aux = A[nInd,:qty].copy()
    A[nInd,:qty], A[nCol,:qty] = A[nCol,:qty] , aux
    return A

def isSquared(A):
    return all(len(row) == len(A) for row in A)

def gaussPartial(A,b):
    res = {}
    # Convert into numpys arr
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    # Appends last column to A matrix
    A = np.concatenate([A, b.reshape((A.shape[0], 1))], axis=1)
    # Validates if matrix is squared
    if not isSquared(np.delete(A, -1, axis=1)):
        res["source"] =  'Not square + 1 col matrix!'
        res["error"] = True
        return res
    # Determines if det is 0
    if (np.linalg.det(np.delete(A, -1, axis=1)) == 0):
        res["source"] =  'Determinant is 0'
        res["error"] = True
        return res
    times = A[:, 0].size - 1
    indexes = np.arange(0, times+1)
    for nCol in range(0,times):
        absCol = np.absolute(A[nCol:,nCol])
        mVal = np.amax(absCol)
        #Validates if there a is biggest number than A[i][i] and swap rows
        if(A[nCol][nCol] < mVal):
            mInd = np.argmax(absCol)
            A,indexes = swapRows(A,nCol,mInd,indexes)
        multipliers = getMultipliers(A,nCol)
        #Validates if any multiplier is different to zero
        if(not np.count_nonzero(multipliers) == 0):
            A = rowOps(A,nCol,multipliers)

    values = customRegresiveSustitution(A,times,indexes)
    res["values"] = values
    res["error"] = False
    return res