
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
        pivots.append({'status':'Step '+str(nCol)})
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
            pivots.append(A)
            pivots.append(L[:,nCol])

    U = A
    pivots.append({'status': 'matrix L'})
    pivots.append(L)
    pivots.append({'status': 'matrix U'})
    pivots.append(U)

    Lb = np.concatenate([L, b.reshape((A.shape[0],1))], axis=1)
    z = progressiveSustitution(Lb, times, indexes)
    z = np.array(z).astype(float)
    Uz = np.concatenate([U, z.reshape((U.shape[0],1))], axis=1)
    print(Uz)
    results = regresiveSustitution(Uz, times-1, indexes)

    return pivots



def showSteps(steps):
    for step in steps:
        try:
            print(pd.DataFrame(step).to_string(index=False, header=False)+"\n")
        except:
            print(step)

def main():
    #luSimple([[0, -2, 1], [20, -7, 12], [-8, 13, 17]], [-12, 13, 31])
    showSteps(luSimple([[0,-2,1],[20,-7,12],[-8,13,17]], [-12,13,31]))


if __name__ == "__main__":
    main()

