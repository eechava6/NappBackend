import numpy as np
import pandas as pd
from utils import regresiveSustitution
from utils import rowOps
from utils import getMultipliers
from utils import swapRows
from utils import swapCols
from utils import isSquared

def gaussTotal(A,b):
    pivots = []
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    A = np.concatenate([A, b.reshape((A.shape[0],1))], axis=1)
    times = A[:,0].size-1
    pivots.append(A.copy())
    if(not isSquared(np.delete(A, -1, axis=1))):
        pivots.append({'status':'Not square + 1 col matrix!'})
        return pivots
    if(np.linalg.det(np.delete(A, -1, axis=1)) == 0):
        pivots.append({'status':'Det 0!'})
        return pivots
    indexes = np.arange(0,times)

    for nCol in range(0,times):
        absMat = np.absolute(A[nCol:,nCol:-1])
        mVal = np.amax(absMat)
        mRow = np.where(absMat == mVal)[0][0]
        mCol = np.where(absMat == mVal)[1][0]

        if (A[nCol][nCol] < mVal):

            if(nCol + mRow != nCol):
                A, indexes = swapRows(A, nCol, mRow, indexes)
                pivots.append(A)

            if(nCol + mCol != nCol):
                A = swapCols(A, nCol, mCol)
                pivots.append(A)

        multipliers = getMultipliers(A, nCol)
        if (not np.count_nonzero(multipliers) == 0):
            A = rowOps(A, nCol, multipliers)
            pivots.append(A)


    values = regresiveSustitution(pivots[-1], times, indexes)
    pivots.append(values)

    return pivots
