import math


def f(x): return math.log(math.pow(math.sin(x),2)+1)-(1/2)

def df(x): return 2*math.pow((math.pow(math.sin(x),2)+1),-1)*math.sin(x)*math.cos(x)

def ddf(x): return math.log(math.pow(math.sin(x),2)+1)-(1/2)-x

def g(x): return math.log(math.pow(math.sin(x),2)+1)-(1/2)
