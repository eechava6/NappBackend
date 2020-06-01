import ast
import json

import numpy as np
from methods.utils import progressiveSustitution, regresiveSustitutions, isSquared


def crout(A,b):
    A = ast.literal_eval(A)
    b = ast.literal_eval(b)
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    pivots = []
    res = {}
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)

    times = A[:, 0].size

    U = np.zeros((times, times))
    L = np.identity(times)
    cont = 0
    # Validates if matrix is squared
    if (not isSquared(A)):
        res["source"] = 'Not square matrix!'
        res["error"] = True
        return res
    # Determines if det is 0
    if (np.linalg.det(A) == 0):
        res["source"] = 'Determinant is 0'
        res["error"] = True
        return res
    #    L,U = inicializa(n,0)

    for d in range(0, times):
        U[d, d] = 1

    for d in range(0, times): #Etapas
        #Calculo L
        for j in range(d, times):
            sum0 = sum([L[j, s] * U[s, d] for s in range(0, j)])
            L[j, d] = A[j, d] - sum0
        #Calculo U
        for j in range(d+1, times):
            sum1 = sum([L[d, s] * U[s, j] for s in range(0, d)])
            U[d, j] = (A[d, j] - sum1) / L[d, d]
        cont = cont+1
        pivots.append({'step': cont, "L": json.dumps(L.tolist()), "U":  json.dumps(U.tolist())})

    LB = np.concatenate([L,b.reshape((A.shape[0],1)) ], axis=1)
    size = LB[:, 0].size

    pro = progressiveSustitution(LB, size)
    pro = np.array(pro).astype(float)

    UB = np.concatenate([U, pro.reshape((U.shape[0], 1))], axis=1)
    size2 = UB[:, 0].size
    results = regresiveSustitutions(UB, size2 - 1)
    res["pivots"] = pivots
    res["error"] = False
    res["results"] = results
    return res




    

