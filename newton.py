# -*- coding: utf-8 -*-

from function import f, df


def newton(x0, tolerance, max_iterations):
    res = {}
    return_list = []
    f_x = float(f(x0))
    df_x = float(df(x0))
    count = 0
    error = tolerance + 1
    return_list.append({"count": count, "xSub0": x0, "f_x": f_x, "df_x": df_x, "error": 0})

    while error > tolerance and count < max_iterations and f_x != 0 and df_x != 0:
        next_x = x0 - (f_x / df_x)
        f_x = f(next_x)
        df_x = df(next_x)
        error = abs(next_x - x0)
        x0 = next_x
        count += 1
        return_list.append({"count": count, "xSub0": x0, "f_x": f_x, "df_x": df_x, "error": error})

    if f_x == 0:
        res["iters"] = return_list
        res["status"] = 'Root found! ;)'
        return res
    elif error <= tolerance:
        res["iters"] = return_list
        res["status"] = 'Err lower than tolerance! :)'
        return res
    elif df_x == 0:
        res["iters"] = return_list
        res["status"] = 'Possible multiple root! :0'
        return res
    elif (count >= max_iterations):
        res["iters"] = return_list
        res["status"] = 'Overpassed max iteration! :('
        return res

    return res
