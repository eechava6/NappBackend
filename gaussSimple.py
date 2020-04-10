
import numpy as np
import pandas as pd
from utils import regresiveSustitution
from utils import rowOps
from utils import getMultipliers
from utils import swapRows

def gaussSimple(A):
    pivots = []
    A = np.array(A).astype(float)
    times = A[:,0].size-1
    pivots.append(A.copy())
    indexes = np.arange(0,times+1)
    for nCol in range(0,times):
        #Validates if A[i][i] is 0 and swap rows to first row with col val != 0 
        if(A[nCol][nCol] == 0):
            partCol = A[nCol:,nCol]
            nInd = np.argmax(partCol > 0)
            if(nInd == 0):
                pivots.append({'status':'This matrix has no solution!'})
                return pivots
            A,indexes = swapRows(A,nCol,nInd,indexes)
            pivots.append(A)
        multipliers = getMultipliers(A,nCol)
        #Validates if any multiplier is different to zero
        if(not np.count_nonzero(multipliers) == 0):
            A = rowOps(A,nCol,multipliers)
            pivots.append(A)
    values = regresiveSustitution(pivots[-1],times,indexes)
    pivots.append(values)
    return pivots

