import ast
import json
import numpy as np
from utils import regresiveSustitution
from utils import rowOps
from utils import getMultipliers
from utils import swapRows
from utils import isSquared

def partialPivot(A,b):
    A = ast.literal_eval(A)
    b = ast.literal_eval(b)
    res = {}
    pivots = []
    # Convert into numpys arr
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    # Appends last column to A matrix
    A = np.concatenate([A, b.reshape((A.shape[0], 1))], axis=1)
    # Validates if matrix is squared
    if not isSquared(np.delete(A, -1, axis=1)):
        res["status"] =  'Not square + 1 col matrix!'
        return res
    # Determines if det is 0
    if (np.linalg.det(np.delete(A, -1, axis=1)) == 0):
        res["status"] =  'Determinant is 0'
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
            pivots.append({"step": nCol, "matrix": json.dumps(A.tolist())})

    values = regresiveSustitution(A,times,indexes)
    res["pivots"] = pivots
    res["values"] = values
    return res