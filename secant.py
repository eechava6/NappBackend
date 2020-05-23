# -*- coding: utf-8 -*-

from function import f


def secant(x0, x1, tolerance, max_iterations):
    res = {}
    return_list = []
    x0_f = float(f(x0))
    if x0_f == 0:
        res["status"] = "root on A"
        return res
    else:
        x1_f = float(f(x1))
        count = 0
        error = tolerance + 1
        denominator = x1_f - x0_f
        return_list.append({'count': count, 'x0': x0, 'f(x)': x0_f, 'error': "N/a"})
        count += 1
        return_list.append({'count': count, 'x0': x1, 'f(x)': x1_f, 'error': "N/a"})
        while error > tolerance and x1_f != 0 and denominator != 0 and count < max_iterations:
            xAux = x1 - ((x1_f * (x1 - x0)) / denominator)
            error = abs(xAux - x1)
            x0 = x1
            x0_f = x1_f
            x1 = xAux
            x1_f = f(x1)
            denominator = x1_f - x0_f
            count += 1
            return_list.append({'count': count, 'x0': xAux, 'f(x)': x0_f, 'error': error})
        if x1_f == 0:
            res["iters"] = return_list
            res["status"] = 'Root found! ;)'
            res["error"] = False
            return res
        elif error <= tolerance:
            res["iters"] = return_list
            res["status"] = 'Err lower than tolerance! :)'
            res["error"] = False
            return res
        elif denominator == 0:
            res["iters"] = return_list
            res["status"] = 'Possible multiple root! :0'
            res["error"] = True
            return res
        elif (count >= max_iterations):
            res["iters"] = return_list
            res["status"] = 'Overpassed max iteration! :('
            res["error"] = True
            return res

        return res
