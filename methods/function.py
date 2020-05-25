from py_expression_eval import Parser
parser = Parser()
f = 0
df = 0;
ddf = 0;
g = 0;

def fDef(stringF):
    global f,parser
    f = parser.parse(stringF)
    return f.toString()

def dfDef(stringF):
    global df,parser
    df = parser.parse(stringF)
    return df.toString()

def ddfDef(stringF):
    global ddf,parser
    ddf = parser.parse(stringF)
    return ddf.toString()

def gDef(stringF):
    global g,parser
    g = parser.parse(stringF)
    return g.toString()

def f(x):
    global f
    return f.evaluate({'x': x})

def df(x):
    global df
    return df.evaluate({'x': x})

def ddf(x):
    global ddf
    return ddf.evaluate({'x': x})

def g(x):
    global g
    return g.evaluate({'x': x})
