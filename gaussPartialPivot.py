
import numpy as np
import pandas as pd
from function import regresiveSustitution
from function import rowOps
from function import getMultipliers

def swapRows(A,nCol,mInd,indexes):
    A[[nCol, mInd+nCol]] = A[[mInd+nCol , nCol]]
    indexes[nCol], indexes[mInd+nCol] = indexes[mInd+nCol], indexes[nCol] 
    return A,indexes

def partialPivot(A):
    pivots = []
    A = np.array(A).astype(float)
    times = A[:,0].size-1
    indexes = np.arange(0,times+1)
    print(indexes)
    for nCol in range(0,times):
        absCol = np.absolute(A[nCol:,nCol])
        mVal = np.amax(absCol)
        #Validates if there a is biggest number than A[i][i] and swap rows
        if(A[nCol][nCol] < mVal):
            mInd = np.argmax(absCol)
            A,indexes = swapRows(A,nCol,mInd,indexes) 
            pivots.append(A)
        multipliers = getMultipliers(A,nCol)
        #Validates if any multiplier is different to zero
        if(not np.count_nonzero(multipliers) == 0):
            A = rowOps(A,nCol,multipliers)
            pivots.append(A)
    values = regresiveSustitution(pivots[-1],times,indexes)
    pivots.append(values)
    return pivots