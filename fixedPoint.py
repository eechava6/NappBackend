from function import f
from function import g
import numpy as np
import math

def fixedPoint (xi,tol,max_iter):
    f_xi = f(xi)
    g_xi = g(xi)
    return_list = []
    return_list.append({
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
        print(f_xi)
        if(f_xi == 0):
            return_list.append({'status':'Root found! ;)'})
            return return_list
        elif(error < tol):
            return_list.append({'status':'Err lower than tolerance! :)'})
            return return_list
        elif(count >= max_iter):
            return_list.append({'status':'Overpassed max iteration! :('})
            return return_list
        count = count + 1

    return return_list




