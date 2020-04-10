
import numpy as np
import pandas as pd
from function import regresiveSustitution
from function import rowOps
from function import getMultipliers

def gaussSimple(A):
    pivots = []
    A = np.array(A).astype(float)
    times = A[:,0].size-1
    pivots.append(A)
    for nCol in range(0,times):
        multipliers = getMultipliers(A,nCol)
        #Validates if any multiplier is different to zero
        if(not np.count_nonzero(multipliers) == 0):
            A = rowOps(A,nCol,multipliers)
            pivots.append(A)
    values = regresiveSustitution(pivots[-1],times)
    pivots.append(values)
    return pivots

def run():
    steps = gaussSimple([[14,6,-2,3,12],[3,15,2,-5,32],[-7,4,-23,2,-24],[1,-3,-2,16,14]])
    for step in steps:
        print(pd.DataFrame(step).to_string(index=False, header=False)+"\n")

run()