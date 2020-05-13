
import numpy as np
import pandas as pd
from utils import regresiveSustitution, progressiveSustitution
from utils import rowOps
from utils import getMultipliers
from utils import swapRows
from utils import isSquared

def luSimple(A,b):
    pivots = []
    #Convert into numpys arr
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)

    #Validates if matrix is squared
    if(not isSquared(A)):
        pivots.append({'status':'Not square + 1 col matrix!'})
        return pivots
    #Determinates if det is 0
    if(np.linalg.det(A) == 0):
        pivots.append({'status':'Det 0!'})
        return pivots

    times = A[:, 0].size
    indexes = np.arange(0, times + 1)

    #matrix L y U
    U = np.zeros([times, times])
    L = np.zeros([times, times])

    for nCol in range(0,times):
        L[nCol, nCol] = 1
        #Validates if A[i][i] is 0 and swap rows to first row in submatrix with col val != 0
        if(A[nCol][nCol] == 0):
            pivots.append({'status': '0 in diagonal'})
            return pivots

        #Calculates the multipliers
        multipliers = getMultipliers(A,nCol)

        # matrix
        for k in range(0, multipliers.size):
            L[(nCol+k)+1,nCol]= multipliers[k]

        #Validates if any multiplier is different to zero
        if(not np.count_nonzero(multipliers) == 0):
            A = rowOps(A,nCol,multipliers)
            pivots.append({'status': 'Step ' + str(nCol), "L": L[:,nCol], "U": A})


    U = A

    Lb = np.concatenate([L, b.reshape((A.shape[0],1))], axis=1)
    z = progressiveSustitution(Lb, times, indexes)
    z = np.array(z).astype(float)
    Uz = np.concatenate([U, z.reshape((U.shape[0],1))], axis=1)
    results = regresiveSustitution(Uz, times-1, indexes)
    pivots.append(results)
    
    return pivots

