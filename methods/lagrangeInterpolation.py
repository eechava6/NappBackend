import numpy as np
import ast

def lagrangeInterpolation(x,y):
    x = ast.literal_eval(x)
    y = ast.literal_eval(y)
    y = np.array(y)
    x = np.array(x)
    nx = len(x)
    res = {}
    Li = []

    # fill the y[i]*L[i]x
    for xi in range(nx):
        Li.append({"numerator": "", "multiplier": 0, "multiplier2": 0})
        auxMultiplier = 1
        for xi2 in range(nx):
            if (xi != xi2):
                auxNumerator = round(-1 * x[xi2],4)
                if (auxNumerator >= 0):
                    auxNumerator = "+" + str(auxNumerator)
                else:
                    auxNumerator = str(auxNumerator)
                Li[xi]['numerator'] += "*(x" + auxNumerator + ")"

                auxMultiplier *= x[xi] - x[xi2]

        Li[xi]['multiplier'] = round(1 / auxMultiplier,4)
        Li[xi]['multiplier2'] = round(y[xi] * (1 / auxMultiplier),4)

    Li.append({"result": ""})

    L = []
    for i in range(0, len(Li) - 1):
        if (Li[i]["multiplier"] >= 0):
            Li[len(Li) - 1]["result"] += "+"

        Li[len(Li) - 1]["result"] += str(Li[i]['multiplier2']) + Li[i]['numerator']
        string = str(round(Li[i]['multiplier'],4))+str((Li[i]['numerator']))
        string = string.replace(" ", "").replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-")
        L.append({"index":i, "L" : string })
    result = Li[len(Li) - 1]["result"]
    result = result.replace(" ", "").replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-")
    res["L"] = L
    res["result"] = result
    return res


