import numpy as np
import pandas as pd
from utils import regresiveSustitution, progressiveSustitution, swapRowsSpecial,regresiveSustitutions
from utils import rowOps
from utils import getMultipliers
from utils import swapRows
from utils import isSquared


def crout(A,HfL):
    U = np.zeros((HfL, HfL))
    L = np.zeros((HfL, HfL))   
    cont = 0
    print("Stage 0")
    print(A)
    for d in range(0, HfL):
        U[d, d] = 1

    for d in range(0, HfL):
        #U[d, d] = 1
        
           
        for j in range(d, HfL):
            sum0 = sum([L[j, s] * U[s, d] for s in range(0, j)]) 
            L[j, d] = A[j, d] - sum0 
        for j in range(d+1, HfL):   
            sum1 = sum([L[d, s] * U[s, j] for s in range(0, d)]) 
            U[d, j] = (A[d, j] - sum1) / L[d, d]
        cont= cont+1
        stage = "Stage" + str(cont)
        print(stage)
        print(L)
        print() 
        print(U)
        print()
        print()    

    return L, U

if __name__ == "__main__":
    A = np.array([[36,3,-4,5],[5,-45,10,-2],[6,8,57,5],[2,3,-8,-42]
])
#[36,3,-4,5],[5,-45,10,-2],[6,8,57,5],[2,3,-8,-42]
    res = crout(A,4)
    L = res[0]
    U = res[1]
    B = np.array([[-20],[69],[96],[-32]])

    #UB = np.concatenate([U,B], axis=1)
    LB = np.concatenate([L, B], axis=1)
    #print(LB)
    size = LB[:,0].size
    print("progresiva LB")
    
    pro = progressiveSustitution(LB,size)
    print(pro)
    pro = np.array(pro).astype(float)
    UB = np.concatenate([U,pro.reshape((U.shape[0],1))], axis=1)
    # Uz = np.concatenate([U, z.reshape((U.shape[0],1))], axis=1)
    print(UB)
    size2 = UB[:,0].size
    print()
    reg = regresiveSustitutions(UB, size2-1)
    print("Regresiva UZ")
    print(reg)
    

    
