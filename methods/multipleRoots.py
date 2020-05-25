from methods.function import f
from methods.function import df
from methods.function import ddf

def multipleRoots (xi,tol,max_iter):
    res = {}
    f_xi = f(xi)
    df_xi = df(xi)
    ddf_xi = ddf(xi)
    return_list = []
    return_list.append({
            'iter':0,
            'xi': xi,
            'f(xi)':f_xi,
            "f'(xi)": df_xi,
            "f''(xi)":ddf_xi,
            'error':'NA'
            })
    count = 1
    error = tol + 1
    while error > tol and count <= max_iter:
        xiTemp = xi
        xi = x_next(xi)
        f_xi = f(xi)
        df_xi = df(xi)
        ddf_xi = ddf(xi)
        error = abs(xi-xiTemp)
        row = {
            'iter':count,
            'xi': xi,
            'f(xi)':f_xi,
            "f'(xi)": df_xi,
            "f''(xi)":ddf_xi,
            'error':error
            }
        return_list.append(row)
        if error <= tol:
            res["iters"] = return_list
            res["status"] = 'Err lower than tolerance! :)'
            res["error"] = False
            return res
        elif (count >= max_iter):
            res["iters"] = return_list
            res["status"] = 'Overpassed max iteration! :('
            res["error"] = True
            return res
        count = count + 1

    return res

def x_next (xn):
    return xn - ((f(xn)*df(xn))/((df(xn)**2)-f(xn)*ddf(xn)))


