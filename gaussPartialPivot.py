
import numpy as np
import pandas as pd
from function import regresiveSustitution
from function import rowOps

def partialPivot(A):
    pivots = []
    A = np.array(A).astype(float)
    pivots.append(A)
    times = A[:,0].size-1
    for nCol in range(0,times):
        absCol = np.absolute(A[nCol:,nCol])
        mVal = np.argmax(absCol)
        if(A[nCol][nCol] < mVal):
            A[[nCol, mVal+nCol]] = A[[mVal+nCol , nCol]]
            pivots.append(A)
        #rowOps validates if it worth, if not returns 0, else returns 
        #switched rows in matrix
        ops = rowOps(A,nCol)
        if(not isinstance(ops,int)):
            A = ops 
            pivots.append(A)
    values = regresiveSustitution(pivots[-1],times)
    pivots.append(values)
    return pivots