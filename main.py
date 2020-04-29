from incrementalSearch import incrementalSearch
from bisection import bisection
from newton import newton
from falseRule import falseRule
from fixedPoint import fixedPoint
from multipleRoots import multipleRoots
from gaussPartialPivot import partialPivot
from gaussSimple import gaussSimple
from gaussTotal import gaussTotal
from secant import secant
from template import template
from LUpivot import luPivot
from LUsimple import luSimple
from crout import crout

import inspect
import pandas as pd
import ast

def incOpt():
    args = inspect.getfullargspec(incrementalSearch)[0]
    return incrementalSearch(*defineParams(args))

def bicOpt():
    args = inspect.getfullargspec(bisection)[0]
    return bisection(*defineParams(args))

def newtonOpt():
    args = inspect.getfullargspec(newton)[0]
    return newton(*defineParams(args))

def falseOpt():
    args = inspect.getfullargspec(falseRule)[0]
    return falseRule(*defineParams(args))

def fixedOpt():
    args = inspect.getfullargspec(fixedPoint)[0]
    return fixedPoint(*defineParams(args))

def secantOpt():
    args = inspect.getfullargspec(secant)[0]
    return secant(*defineParams(args))

def multipleOpt():
    args = inspect.getfullargspec(multipleRoots)[0]
    return multipleRoots(*defineParams(args))

def simpleOpt():
    args = inspect.getfullargspec(gaussSimple)[0]
    return gaussSimple(*defineParams(args))    

def partialOpt():
    args = inspect.getfullargspec(partialPivot)[0]
    return partialPivot(*defineParams(args))

def gaussTotalOpt():
    args = inspect.getfullargspec(gaussTotal)[0]
    return gaussTotal(*defineParams(args))

def luPivotOpt():
    args = inspect.getfullargspec(luPivot)[0]
    return luPivot(*defineParams(args))

def crout():
    args = inspect.getfullargspec(crout)[0]
    return crout(*defineParams(args))    

def luSimpleOpt():
    args = inspect.getfullargspec(luSimple)[0]
    return luSimple(*defineParams(args))

def templateOpt():
    args = inspect.getfullargspec(template)[0]
    return template(*defineParams(args))

def main():
    print(
    '0 for template\n'
    '1 for incremental search\n'
    '2 for bisection\n'
    '3 for false rule\n'
    '4 for newton\n'
    '5 for fixed point\n'
    '6 for secant\n'
    '7 for multiple roots\n'
    '8 for gauss simple\n'
    '9 for gauss partial pivot\n'
    '10 for gauss total pivot\n'
    '11 for lu simple \n'
    '12 for lu pivot \n'
    '13 for lu crout \n'
    )

    option = int(input())

    switch = {
        0: templateOpt,
        1: incOpt,
        2: bicOpt,
        3: falseOpt,
        4: newtonOpt,
        5: fixedOpt,
        6: secantOpt,
        7: multipleOpt,
        8: simpleOpt,
        9: partialOpt,
        10: gaussTotalOpt,
        11: luSimpleOpt,
        12: luPivotOpt,
        13: crout
    }

    func = switch.get(option, lambda: [{ 'status' : "Invalid option!!"}])
    if(option <= 7):
        showTable(func())
    else:
        #[[-7, 2, -3, 4], [5, -1, 14, -1], [ 1 , 9, -7, 5], [-12, 13, -8, -4]]
        #[-32, 31 , 13 , -12]
        #[[-7,2,-3,4],[5,-1,14,-1],[1,9,-7,5],[-28,13,-8,-4]] [-12,13,31,-32]
        #[[1,2,2,4,8],[0,1,1,5,9],[0,0,0,7,10],[0,0,1,8,11]]
        showSteps(func())
        return 0


def defineParams(params):
    values = []
    for param in params:
        print('Enter %s ' % (param))
        value = input()
        try:
            values.append(float(value))
        except:
            values.append(ast.literal_eval(value))
    print('')
    return values

def showSteps(steps):
    for step in steps:
        try:
            print(pd.DataFrame(step).to_string(index=False, header=False)+"\n")
        except:
            print(step)
    
def showTable(table):
    result = ""
    if('status' in table[-1]):
        result = table[-1]
        table.pop()
    print(pd.DataFrame(table).to_string(index=False))
    print(result)

if __name__ == "__main__":
    main()
