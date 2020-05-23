import numpy as np
import json as js

def vandermonde(x,y):
    yT = y.T
    print("Transpose Y: ")
    print(yT)

    invX = np.linalg.inv(vanx)
    #print("inv X: ")
    #print(invX)

    dotPoint = np.dot(invX,yT)
    #print("dot point (x,y): ")
    #print(dotPoint)

    sizePol = len(dotPoint)

    countPol = sizePol

    print("The polinom is: ")
    for i in range(sizePol):
        print(dotPoint[i],"x",countPol-1,"+ ",end=" ")
        countPol -= 1
        if(countPol == 1):
            break
    print(dotPoint[sizePol-1])

    n = 2
    pol = np.polyval(dotPoint,n)
    print("The polinom evaluated in",n,"is: ")
    print(pol)

    result = {
        'x': x,
        'vandermondeMat': vanx,
        'transposeY': yT,
        'polinom': dotPoint
    }
    return result


x = np.array( [-1,1,-0.64745,6]) # x coordinates in space
y = np.array( [1,3,1,-2]) # f(x)
print("x: ")
print(x)
print("Van der monde Matrix x: ")
vanx = np.vander(x)
print(vanx)

res = vandermonde(x,y)
print("------------")
print(res['x'])
print(res['transposeY'])
print(res['vandermondeMat'])
print(res['polinom'])

# if you want to evaluate uncomment polyval (polinom, point)

# before
#p = np.dot(np.linalg.inv(np.vander(x)),y.T)

#print("Polinom: ")
#print(p)