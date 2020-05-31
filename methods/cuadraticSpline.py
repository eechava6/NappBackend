import numpy as np
from methods.utils import gaussTotal

def cubic_interp1d(x, y):
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

    values = gaussTotal(A,b)
    if values["error"]:
        res["error"] = True
        res["source"] = values["source"]

    vals = sorted(values["values"], key = lambda x:  x[0])
    pols = []
    for val in range(0,len(vals)-1,2):
        pol = "{0}*x+{1}".format(vals[val][1], vals[val+1][1])
        pol = pol.replace(" ", "").replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-")
        S.append([vals[val][0], vals[val+1][1]])
        pols.append(pol)
    res["polynoms"] = pols
    res["vals"] = vals
    res["error"] = False
    res["matrix"] = A
    return res

if __name__ == '__main__':
    x = np.array([-2,-1,2,3])
    y = np.array([12.1353, 6.3678, -4.61094, 2.0855])
    print( cubic_interp1d(x, y))
