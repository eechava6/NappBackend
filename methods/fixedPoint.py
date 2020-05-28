from methods.function import f
from methods.function import g


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
    if (f_xi == 0):
        res["iters"] = return_list
        res["status"] = 'Root found! ;)'
        res["error"] = False
        return res
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
            res["error"] = False
            return res
        elif(error < tol):
            res["iters"] = return_list
            res["status"] = 'Err lower than tolerance! :)'
            res["error"] = False
            return res
        elif(count >= max_iter):
            res["iters"] = return_list
            res["status"] = 'Overpassed max iteration! :('
            res["error"] = True
            return res
        count = count + 1

    return {"iters" : return_list}




