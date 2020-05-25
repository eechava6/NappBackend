import numpy as np
import ast

def vandermonde(x,y):
    x = ast.literal_eval(x)
    y = ast.literal_eval(y)
    y = np.array(y)
    x = np.array(x)
    vanx = np.vander(x)
    yT = y.T
    invX = np.linalg.inv(vanx) # Get the inverse of matrix x
    dotPoint = np.dot(invX,yT) # dot point between inverse x and transpose Y
    sizePol = len(dotPoint)
    countPol = sizePol
    polynom = ""
    for i in range(sizePol):
        polynom += str(np.round(dotPoint[i],4))+ "*x^"+str(countPol-1)+"+"
        countPol -= 1
        if(countPol == 1):
            break
    polynom += str(round(dotPoint[sizePol-1],4))
    polynom = polynom.replace(" ", "").replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-")
    results = {
        'vMatrix': vanx.tolist(),
        'values': np.round(dotPoint,14).tolist(),
        'polynom': polynom
    }
    return results
