# -*- coding: utf-8 -*-

from function import f


def bisection(a, b, tolerance, max_iterators):
    res = {}
    return_list = []
    a_evaluated_f = float(f(a))
    b_evaluated_f = float(f(b))
    if a_evaluated_f == 0:
        return {"status" : "root on A"}
    elif b_evaluated_f == 0:
        return {"status": "root on B"}
    elif a_evaluated_f * b_evaluated_f < 0:
        count = 1
        x_middle = float((a + b) / 2)
        y_middle = float(f(x_middle))
        error = tolerance + 1
        row = {
                'x' : count,
                'a' : a,
                'b' : b,
                'x_middle': x_middle,
                'y_middle': y_middle,
                'error': 0
        }
        return_list.append(row)
        count += 1
        while error > tolerance and y_middle != 0 and count <= max_iterators:
            if a_evaluated_f * y_middle < 0:

                b = x_middle
                b_evaluated_f = y_middle
            else:
                a = x_middle
                a_evaluated_f = y_middle
            aux_middle = x_middle
            x_middle = (a + b) / 2
            y_middle = f(x_middle)
            error = abs(x_middle - aux_middle)

            row = {
                'x' : count,
                'a' : a,
                'b' : b,
                'x_middle': x_middle,
                'y_middle': y_middle,
                'error': error
            }
            count += 1
            return_list.append(row)
            if (y_middle == 0):
                res["iters"] = return_list
                res["status"] = 'Root found! ;)'

                return res
            elif (error < tolerance):
                res["iters"] = return_list
                res["status"] = 'Err lower than tolerance! :)'
                return res
            elif (count >= max_iterators):
                res["iters"] = return_list
                res["status"] =  'Overpass max iteration! :('
                return res


    return res



