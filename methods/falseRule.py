from methods.function import f

def falseRule (xi,xs,tol,max_iter):
    res = {}
    xr = evaluateFunction(xi,xs)
    f_xr = f(xr)
    return_list = []
    return_list.append({
            'iter': 1,
            'xi': xi,
            'xs' : xs,
            'xr': xr,
            'f(xr)': f_xr,
            'error':'NA'
            })
    count = 2
    error = tol + 1
    while error > tol and count <= max_iter:
        xi = xr if (f_xr < 0) else xi
        xs = xr if (f_xr > 0) else xs
        tempXr = xr
        xr = evaluateFunction( xi, xs)
        error = abs(xr - tempXr)
        f_xr = f(xr)

        row = {
            'iter' : count,
            'xi': xi,
            'xs' : xs,
            'xr': xr,
            'f(xr)': f_xr,
            'error': error
            }
        return_list.append(row)
        if f_xr == 0:
            res["iters"] = return_list
            res["status"] = 'Root found! ;)'
            res["error"] = False

            return res
        elif error < tol:
            res["iters"] = return_list
            res["status"] = 'Err lower than tolerance! :)'
            res["error"] = False

            return res
        elif count >= max_iter:
            res["iters"] = return_list
            res["status"] =  'Overpass max iteration! :('
            res["error"] = True
            return res
        count = count + 1
    return res

def evaluateFunction(xi,xs):
    return xi - ((f(xi)*(xs-xi))/(f(xs)-f(xi)))



