from function import f
import numpy as np
import math

def template (xi,tol,max_iter):
    f_x = evaluateFunction(xi)
    return_list = []
    return_list.append({
            'iter': 1,
            'xi': xi,
            'f(x)': f_x,
            'error':'NA'
            })
    count = 2
    error = tol + 1 
    while error > tol and count <= max_iter:
        xi = f_x
        f_x = evaluateFunction(xi)
        
        error = abs(xi - f_x)
        
        row = {
            'iter' : count,
            'xi': xi,
            'f(x)': f_x,
            'error': error
            }
        return_list.append(row)
        if(f_x == 0):
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

def evaluateFunction(xi):
    part1 = f(xi)**2
    part2 = f(xi+f(xi))
    part3 = f(xi)
    return xi - (part1/(part2-part3))

