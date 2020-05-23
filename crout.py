import numpy as np
import pandas as pd
from utils import regresiveSustitution, progressiveSustitution, swapRowsSpecial,regresiveSustitutions
from utils import rowOps
from utils import getMultipliers
from utils import swapRows
from utils import isSquared


def crout(A,b):

    pivots = []

    A = np.array(A).astype(float)
    b = np.array(b).astype(float)

    times = A[:, 0].size

    U = np.zeros((times, times))
    L = np.identity(times)
    cont = 0

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
        pivots.append({'status':'Step '+str(cont), 'matrixL': L.copy(), 'matrixU': U.copy()})

    LB = np.concatenate([L, b], axis=1)
    size = LB[:, 0].size

    pro = progressiveSustitution(LB, size)
    pro = np.array(pro).astype(float)

    UB = np.concatenate([U, pro.reshape((U.shape[0], 1))], axis=1)
    size2 = UB[:, 0].size
    reg = regresiveSustitutions(UB, size2 - 1)
    pivots.append({'status':'Results', 'reg': reg})

    return pivots


def showSteps(steps):
    for step in steps:
        try:
            print(pd.DataFrame(step).to_string(index=False, header=False)+"\n")
        except:
            print(step)

def showTable(table):
    result = ""
    if('status' in table[-1]):
        result = table[-1]
        table.pop()
    print(pd.DataFrame(table).to_string(index=False))
    print(result)

if __name__ == "__main__":
    A = [[4, -1, 0, 3],[1, 15.5, 3, 8],[0, -1.3, -4, 1.1],[14, 5, -2, 30]]
    B = [[1],[1],[1],[1]]

    results = crout(A,B)

    for r in range(0,len(results)-1):
        print(results[r]['status'])
        print("matrix L")
        showTable(results[r]['matrixL'])
        print("matrix U")
        showTable(results[r]['matrixU'])

    print("Results")
    print(results[len(results)-1]['reg'])





    

