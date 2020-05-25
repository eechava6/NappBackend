import numpy as np
import ast
import json
from methods.utils import regresiveSustitution
from methods.utils import rowOps
from methods.utils import getMultipliers
from methods.utils import swapRows
from methods.utils import swapCols
from methods.utils import isSquared

def gaussTotal(A,b):
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
        res["error"] = True
        return res
    # Determines if det is 0
    if (np.linalg.det(np.delete(A, -1, axis=1)) == 0):
        res["status"] =  'Determinant is 0'
        res["error"] = True
        return res
    times = A[:, 0].size - 1
    indexes = np.arange(0, times+1)
    for nCol in range(0,times):
        absMat = np.absolute(A[nCol:,nCol:-1])
        mVal = np.amax(absMat)
        mRow = np.where(absMat == mVal)[0][0]
        mCol = np.where(absMat == mVal)[1][0]

        if (A[nCol][nCol] < mVal):
            if(nCol + mRow != nCol):
                A, indexes = swapRows(A, nCol, mRow, indexes)
            if(nCol + mCol != nCol):
                A = swapCols(A, nCol, mCol)

        multipliers = getMultipliers(A, nCol)
        # Validates if any multiplier is different to zero
        if (not np.count_nonzero(multipliers) == 0):
            A = rowOps(A, nCol, multipliers)
            pivots.append({"step": nCol, "matrix": json.dumps(A.tolist())})

    values = regresiveSustitution(A,times,indexes)
    res["pivots"] = pivots
    res["values"] = values
    res["error"] = False
    return res
