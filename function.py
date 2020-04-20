import math


def f(x): return (x**2 - x + 1.25 - math.exp(x))

def df(x): return math.exp(x)-1

def ddf(x): return math.exp(x)

def g(x): return math.log(math.pow(math.sin(x),2)+1)-(1/2)
