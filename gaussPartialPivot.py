
import numpy as np
import pandas as pd


def swapMaxAbs(Ab,nCol):
    absCol = np.absolute(Ab[nCol:,nCol])
    mVal = np.argmax(absCol)
    Ab[[nCol, mVal+nCol]] = Ab[[mVal+nCol , nCol]]
    return Ab

def rowOps(Ab,nCol):
    col = Ab[:,nCol]
    f = lambda x: x/col[nCol]
    multipliers = f(col)
    multipliers = multipliers[nCol+1:]
    pivot = np.tile(Ab[nCol,:],(col.size-nCol-1,1))
    mMatrix = (pivot.transpose()*multipliers).transpose()
    arr = getArr(nCol)
    r = np.delete(Ab,arr,0) - mMatrix
    for val in reversed(arr):
        r = np.insert(r,0,[Ab[val,:]],0)
    return r

def getArr(n):
    arr = []
    for val in range(0,n+1):
        arr.append(val)
    return arr

def partialPivot(A):
    pivots = []
    A = np.array(A).astype(float)
    pivots.append(A)
    times = A[:,0].size-1
    for index in range(0,times):
        maxA = swapMaxAbs(A,index)
        pivots.append(maxA)
        A = rowOps(maxA,index)
        pivots.append(A)
    return pivots