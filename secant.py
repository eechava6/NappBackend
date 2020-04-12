# -*- coding: utf-8 -*-

from function import f


def secant(x0, x1, tolerance, max_iterations):

    return_list = []

    x0_f = float(f(x0))

    if x0_f == 0:
        print(str(x0) + " is  a root")
    else:

        x1_f = float(f(x1))
        count = 0
        error = tolerance + 1

        denominator = x1_f - x0_f

        return_list.append({'count': count, 'x0': x0, 'f(x)': x0_f, 'error': 0})

        while error > tolerance and x1_f != 0 and denominator != 0 and count < max_iterations:

            xAux = x1 - ((x1_f * (x1 - x0)) / denominator)

            error = abs(xAux - x1)

            x0 = x1
            x0_f = x1_f

            x1 = xAux
            x1_f = f(x1)
        
            denominator = x1_f - x0_f

            count += 1

            return_list.append({'count': count, 'x0': x0, 'f(x)': x0_f, 'error': error})

        if x1_f == 0:
            print(str(x1) + "is a root")
        elif denominator == 0:
            print("possible multiple root")

        return return_list

