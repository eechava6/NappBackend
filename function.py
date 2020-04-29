import math

def f(x):
    first = 1/math.sqrt((1.5175**2)-1)
    firstBig = first*(1.5175-x)
    return math.sqrt(1-(x**2)) - firstBig

def df(x): return 0.876113 - (x/math.sqrt(1-(x**2)))

def ddf(x): return math.exp(x)

def g(x): return math.sqrt(1-(x**2))
