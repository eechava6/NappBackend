from incrementalSearch import incrementalSearch
from bisection import bisection
from newton import newton
from falseRule import falseRule
from fixedPoint import fixedPoint
from multipleRoots import multipleRoots
from gaussPartialPivot import partialPivot

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

def multipleOpt():
    args = inspect.getfullargspec(multipleRoots)[0]
    return multipleRoots(*defineParams(args))

def partialOpt():
    args = inspect.getfullargspec(partialPivot)[0]
    return partialPivot(*defineParams(args))

def main():
    print('1 for incremental search\n'
    '2 for bisection\n'
    '3 for false rule\n'
    '4 for newton\n'
    '5 for fixed point\n'
    '7 for multiple roots\n'
    '9 for gauss partial pivot\n')

    option = int(input())

    switch = {
        1: incOpt,
        2: bicOpt,
        3: falseOpt,
        4: newtonOpt,
        5: fixedOpt,
        7: multipleOpt,
        9: partialOpt
    }

    func = switch.get(option, lambda: [{ 'status' : "Invalid option!!"}])
    if(option <= 7):
        showTable(func())
    else:
        #[[-7,2,-3,4,-12],[5,-1,14,-1,13],[1,9,-7,5,31],[-12,13,-8,-4,-32]]
        #[[1,2,3,4,8],[0,5,6,5,9],[0,0,9,7,10],[0,0,0,8,11]]
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
        print(pd.DataFrame(step).to_string(index=False, header=False)+"\n")
    
def showTable(table):
    result = ""
    if('status' in table[-1]):
        result = table[-1]
        table.pop()
    print(pd.DataFrame(table).to_string(index=False))
    print(result)

if __name__ == "__main__":
    main()
