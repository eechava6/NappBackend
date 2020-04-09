from function import f
import numpy as np

def incrementalSearch (start, step, stop):
    decimals = 4
    return_list = []
    evaluated = f(start)
    return_list.append({
            'x': start,
            'f(x)' : evaluated,
            'root': 'NA',
            'f(a)*f(b)': 'NA',
            'range':'NA'
            })
    points = np.arange(start+step,stop,step)

    for point in points:
        mult = float(evaluated * f(point))
        root = True if mult < 0 else False 
        row = {
            'x': point,
            'f(x)' : round(f(point), decimals),
            'root': root,
            'f(a)*f(b)':round(mult,decimals),
            'range':[round(point-step,decimals),round(point,decimals)]
            }
        return_list.append(row)
        evaluated = f(point)

    return return_list




