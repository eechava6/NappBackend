
import numpy as np
import ast
import json
from utils import regresiveSustitution, progressiveSustitution
from utils import rowOps
from utils import getMultipliers
from utils import isSquared

def luSimple(A,b):
    A = ast.literal_eval(A)
    b = ast.literal_eval(b)
    res = {}
    pivots = []
    # Convert into numpys arr
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)

    # Validates if matrix is squared
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
    #matrix L
    L = np.identity(times)

    for nCol in range(0,times):
        L[nCol, nCol] = 1
        #Validates if A[i][i] is 0 and swap rows to first row in submatrix with col val != 0
        if(A[nCol][nCol] == 0):
            res["status"] = '0 in diagonal!'
            return res

        #Calculates the multipliers
        multipliers = getMultipliers(A,nCol)

        # matrix
        for k in range(0, multipliers.size):
            print(L)
            L[(nCol+k)+1,nCol]= multipliers[k]

        #Validates if any multiplier is different to zero
        if(not np.count_nonzero(multipliers) == 0):
            A = rowOps(A,nCol,multipliers)
        pivots.append({'step': nCol, "L":json.dumps(L.tolist()) , "U": json.dumps(A.tolist())})

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

