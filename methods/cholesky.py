import ast
import json
from math import sqrt
import numpy as np

# Cholesky
from methods.utils import isSquared, progressiveSustitution, regresiveSustitution


def cholesky(A, b):
    A = ast.literal_eval(A)
    b = ast.literal_eval(b)
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    n = len(A[0])
    rows = len(A)
    columns = len(A[0])
    L = np.zeros((rows, columns), float)
    U = np.zeros((rows, columns), float)

    res = {}
    pivots = []
    #Validates if is positive defined
    if not (np.all(np.linalg.eigvals(A) > 0) == True):
        res["source"] = 'Not real solution!'
        res["error"] = True
        return res
    #Validates if matrix is squared
    if(not isSquared(A)):
        res["source"] =  'Not square matrix!'
        res["error"] = True
        return res
    # Determines if det is 0
    if(np.linalg.det(A) == 0):
        res["source"] =  'Determinant is 0'
        res["error"] = True
        return res

    for k in range(0, rows):
        suma = 0.0
        for p in range(0, k):
            suma = suma + L[k][p] * U[p][k]
        L[k][k] = sqrt(A[k][k] - suma)
        U[k][k] = L[k][k]

        for i in range(k, rows):
            suma = 0
            for p in range(0, k):
                suma = suma + L[i][p] * U[p][k]
            L[i][k] = (A[i][k] - suma) / L[k][k]

        for j in range(k, rows):
            suma = 0
            for p in range(0, k):
                suma = suma + L[k][p] * U[p][j]
            U[k][j] = (A[k][j] - suma) / L[k][k]
        #imprimir L  U y k etapa
        pivots.append({'step': k, "L": json.dumps(L.tolist()), "U":  json.dumps(U.tolist())})

    Lb = np.concatenate([L,b.reshape((A.shape[0],1)) ], axis=1)
    indexes = np.arange(0, n)
    z = progressiveSustitution(Lb, n, indexes)
    z = np.array(z).astype(float)
    Uz = np.concatenate([U, z.reshape((U.shape[0],1))], axis=1)
    results = regresiveSustitution(Uz, n-1, indexes)

    res["pivots"] = pivots
    res["error"] = False
    res["results"] = results
    return res