
import numpy as np
import ast
import json
from utils import regresiveSustitution, progressiveSustitution, swapRowsSpecial
from utils import rowOps
from utils import getMultipliers
from utils import swapRows
from utils import isSquared
def luPivot(A,b):
    A = ast.literal_eval(A)
    b = ast.literal_eval(b)
    res = {}
    pivots = []
    #Convert into numpys arr
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    
    #Validates if matrix is squared
    if(not isSquared(A)):
        res["status"] =  'Not square + 1 col matrix!'
        res["error"] = True
        return res
    # Determines if det is 0
    if(np.linalg.det(A) == 0):
        res["status"] =  'Determinant is 0'
        res["error"] = True
        return res

    times = A[:, 0].size
    indexes = np.arange(0, times)


    #matrix L y U
    L = np.identity(times)
    P = np.identity(times)

    for nCol in range(0,times):

        L[nCol, nCol] = 1

        absCol = np.absolute(A[nCol:,nCol])
        mVal = np.amax(absCol)
        swap = False
        #Validates if there a is biggest number than A[i][i] and swap rows
        mInd = np.argmax(absCol)

        if(A[nCol][nCol] < mVal):
            A,indexes = swapRows(A,nCol,mInd,indexes)
            P,b = swapRows(P,nCol,mInd,b)
            swap = True

        multipliers = getMultipliers(A,nCol)
        # matrix
        for k in range(0, multipliers.size):
            L[(nCol + k) + 1, nCol] = multipliers[k]
        if (swap == True):
            L = swapRowsSpecial(L, nCol, mInd+nCol)
        #Validates if any multiplier is different to zero
        if(not np.count_nonzero(multipliers) == 0):
            A = rowOps(A,nCol,multipliers)
        pivots.append({'step': nCol, "L": json.dumps(L.tolist()), "U": json.dumps(A.tolist()), "P" : json.dumps(P.tolist())})

    U = A
    Lb = np.concatenate([L, b.reshape((A.shape[0],1))], axis=1)
    z = progressiveSustitution(Lb, times, indexes)
    z = np.array(z).astype(float)
    Uz = np.concatenate([U, z.reshape((U.shape[0],1))], axis=1)
    results = regresiveSustitution(Uz, times-1, indexes)
    res["pivots"] = pivots
    res["results"] = results
    res["error"] = False

    return res

