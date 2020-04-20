import math


def f(x): return math.exp(x)-x-1

def df(x): return math.exp(x)-1

def ddf(x): return math.exp(x)

def g(x): return math.log(math.pow(math.sin(x),2)+1)-(1/2)
