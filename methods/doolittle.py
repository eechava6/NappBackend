import ast
import json
import numpy as np
from methods.utils import isSquared, progressiveSustitution, regresiveSustitution


def doolittle(A, b):
    A = ast.literal_eval(A)
    b = ast.literal_eval(b)
    n = len(A[0])
    A = np.array(A).astype(float)
    b = np.array(b).astype(float)
    U = np.zeros((n,n))
    L = np.eye(n, dtype=float)
    res = {}
    pivots = []
    diag=1
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
#    L,U = inicializa(n,0)
    for k in range(n):
        suma1 = 0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        U[k][k] = A[k][k]-suma1
        for i in range(k+1,n):
            suma2 = 0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/float(U[k][k])
        for j in range(k+1,n):
            suma3 = 0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/float(L[k][k])
        #imprimir L  U y k etapa
        pivots.append({'step': k, "L": json.dumps(L.tolist()), "U":  json.dumps(U.tolist())})

    Lb = np.concatenate([L,b.reshape((A.shape[0],1)) ], axis=1)
    for i in range(0,n):
        diag = diag*U[i][i]
    if(diag != 0):
        indexes = np.arange(0, n)
        z = progressiveSustitution(Lb, n, indexes)
        z = np.array(z).astype(float)
        Uz = np.concatenate([U, z.reshape((U.shape[0], 1))], axis=1)
        results = regresiveSustitution(Uz, n - 1, indexes)
    else:
        res["source"] = 'Infinite solutions'
        res["error"] = True
        return res

    res["pivots"] = pivots
    res["error"] = False
    res["results"] = results
    return res
