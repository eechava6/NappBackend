from incrementalSearch import incrementalSearch
from bisection import bisection
from newton import newton
from falseRule import falseRule
from fixedPoint import fixedPoint
from multipleRoots import multipleRoots
import inspect 
import pandas as pd

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

def main():
    print('1 for incremental search\n'
    '2 for bisection\n'
    '3 for false rule\n'
    '4 for newton\n'
    '5 for fixed point\n'
    '7 for multiple roots\n')

    option = int(input())
    
    switch = {
        1: incOpt,
        2: bicOpt,
        3: falseOpt,
        4: newtonOpt,
        5: fixedOpt,
        7: multipleOpt
    }

    func = switch.get(option, lambda: [{ 'status' : "Invalid option!!"}])
    showTable(func())


def defineParams(params):
    values = []
    for param in params:
        print('Enter %s ' % (param)) 
        values.append(float(input()))
    print('')
    return values

def showTable(table):
    result = ""
    if('status' in table[-1]):
        result = table[-1]
        table.pop()
    print(pd.DataFrame(table).to_string(index=False))
    print(result)

if __name__ == "__main__":
    main()
