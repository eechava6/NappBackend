import ast
import json

import numpy as np
from methods.utils import gaussPartial


def linearSpline(x, y):
    x = ast.literal_eval(x)
    y = ast.literal_eval(y)

    res = {}
    x = np.asfarray(x)
    y = np.asfarray(y)
    n = len(x)
    m = 2*(n-1)
    A = np.zeros([m,m])
    b = np.zeros([m,1])
    S = []

    if n != len(y):
        res["source"] = "X and Y boundaries are different"
        res["error"] = True
        return

    A[0][0:2] = [x[0], 1]
    b[0] = y[0]
    for val in range(1,n):
        A[val][ 2*val-2:2*val] = [x[val],1]
        b[val] = y[val]

    for val in range(1,n-1):
        A[n-1+val][2*val-2:2*val+2] = [x[val], 1, -x[val], -1]

    values = gaussPartial(A,b)
    if values["error"]:
        res["error"] = True
        res["source"] = values["source"]
        return res

    vals = sorted(values["values"], key = lambda x:  x[0])
    pols = []
    for val in range(0,len(vals)-1,2):
        vals[val][1] =  round(vals[val][1],4)
        vals[val + 1][1] =  round( vals[val + 1][1],4)
        pol = "{0}*x+{1}".format(vals[val][1], vals[val+1][1])
        pol = pol.replace(" ", "").replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-")
        S.append([vals[val][1], vals[val+1][1]])
        pols.append(pol)
    A = np.array(A).astype(float)
    S = np.array(S).astype(float)
    res["polynoms"] = pols
    res["values"] = S.tolist()
    res["error"] = False
    res["matrix"] = json.dumps(A.tolist())
    return res
