
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

