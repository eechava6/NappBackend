# -*- coding: utf-8 -*-

from function import f, df


def newton(x0, tolerance, max_iterations):

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
        print(str(x0) + " is a root")
    elif error <= tolerance:
        print(str(x0) + " is an approximation with tolerance " + str(tolerance))
    elif df_x == 0:
        print(str(next_x) + " is a possible multiple root")
    else:
        print("maximum iterations reached")
    
    return return_list
