import numpy as np

def vandermonde(x,y):
    vanx = np.vander(x)
    yT = y.T

    invX = np.linalg.inv(vanx) # Get the inverse of matrix x

    dotPoint = np.dot(invX,yT) # dot point between inverse x and transpose Y

    sizePol = len(dotPoint)

    countPol = sizePol


    print("The polinom is: ")
    for i in range(sizePol):
        print(np.round(dotPoint[i],14),"x",countPol-1,"+ ",end=" ")
        countPol -= 1
        if(countPol == 1):
            break
    print(dotPoint[sizePol-1])

    n = 0.5 # replace it to get the value of the polynom in this point
    pol = np.polyval(dotPoint,n)
    print("The polinom evaluated in",n,"is: ")
    print(pol)

    result = {
        'vandermondeMat': vanx,
        'polinom': np.round(dotPoint,14)
    }
    return result


x = np.array([-1,1,5.992,6])
print("Van der monde Matrix x: ")

y = np.array([1,3,-1,-2])
res = vandermonde(x,y)
print("------------")
print(res['vandermondeMat'])
print(res['polinom'])