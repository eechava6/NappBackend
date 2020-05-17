from function import f
from function import g
import numpy as np
import math

def fixedPoint (xi,tol,max_iter):
    res = {}
    f_xi = f(xi)
    g_xi = g(xi)
    return_list = []
    return_list.append({
            'iter':0,
            'xi': xi,
            'g(xi)':g_xi,
            'f(xi)': f_xi,
            'error':'NA'
            })
    count = 1
    error = tol + 1
    while error > tol and count <= max_iter:
        xn = g_xi
        g_xi = g(xn)
        f_xi = f(xn)
        error = abs(xn-xi)
        xi = xn
        row = {
            'iter' : count,
            'xi': xi,
            'g(xi)':g_xi,
            'f(xi)': f_xi,
            'error': error
            }
        return_list.append(row)
        if(f_xi == 0):
            res["iters"] = return_list
            res["status"] = 'Root found! ;)'
            return res
        elif(error < tol):
            res["iters"] = return_list
            res["status"] = 'Err lower than tolerance! :)'
            return res
        elif(count >= max_iter):
            res["iters"] = return_list
            res["status"] = 'Overpassed max iteration! :('
            return res
        count = count + 1

    return {"iters" : return_list}




