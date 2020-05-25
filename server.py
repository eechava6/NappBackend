from methods.incrementalSearch import incrementalSearch
from methods.bisection import bisection
from methods.newton import newton
from methods.falseRule import falseRule
from methods.fixedPoint import fixedPoint
from methods.multipleRoots import multipleRoots
from methods.gaussPartialPivot import partialPivot
from methods.gaussSimple import gaussSimple
from methods.gaussTotal import gaussTotal
from methods.secant import secant
from methods.LUpivot import luPivot
from methods.LUsimple import luSimple
from methods.gaussSeidel import gaussSeidel
from methods.jacobi import jacobi
from methods.sor import sor
from methods.newtonInterpolation import newtonInterpolation
from methods.vandermonde import  vandermonde
from methods.lagrangeInterpolation import lagrangeInterpolation

from utils.defFunction import defFunction

from views.home import methods

from flask import Flask, request


app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    return methods()

@app.route("/incSearch",methods=['POST'])
def incSearch():
    data = request.json
    start = data["start"]
    step = data["step"]
    end = data["end"]
    f = data["f"]
    f = defFunction(f,"f")
    method = dict(incrementalSearch(start,step,end))
    return { "f" : f, "method" : method}

@app.route("/bisection",methods=['POST'])
def bisect():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    f = data["f"]
    f = defFunction(f,"f")
    method = dict(bisection(a,b,tol,iters))
    return {"f": f, "method": method}

@app.route("/falseRule",methods=['POST'])
def falRule():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    f = data["f"]
    f = defFunction(f,"f")
    method = falseRule(a,b,tol,iters)
    return {"f": f, "method": method}

@app.route("/newton",methods=['POST'])
def newt():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    f = data["f"]
    f = defFunction(f,"f")
    df = data["df"]
    df = defFunction(df,"df")
    method = dict(newton(a,tol,iters))
    return  {"f": f, "df": df, "method": method}

@app.route("/fixedPoint",methods=['POST'])
def fixPoint():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    f = data["f"]
    f = defFunction(f, "f")
    g = data["g"]
    g = defFunction(g, "g")
    method = dict(fixedPoint(a,tol,iters))
    return {"f": f, "g": g, "method": method}

@app.route("/secant",methods=['POST'])
def seca():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    f = data["f"]
    f = defFunction(f, "f")
    method =  dict(secant(a,b,tol,iters))
    return {"f": f, "method": method}

@app.route("/multipleRoots",methods=['POST'])
def multiRoot():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    f = data["f"]
    f = defFunction(f, "f")
    df = data["df"]
    df = defFunction(df,"df")
    ddf = data["ddf"]
    ddf = defFunction(ddf,"ddf")
    data = dict(multipleRoots(a,tol,iters))
    return {"f" : f, "df" : df, "ddf" : ddf, "method" : data}

@app.route("/gaussSimple",methods=['POST'])
def gaussSimp():
    data = request.json
    a = data["a"]
    b = data["b"]
    return dict(gaussSimple(a,b))

@app.route("/gaussPartial",methods=['POST'])
def gaussPart():
    data = request.json
    a = data["a"]
    b = data["b"]
    return dict(partialPivot(a, b))

@app.route("/gaussTotal",methods=['POST'])
def gaussTot():
    data = request.json
    a = data["a"]
    b = data["b"]
    return dict(gaussTotal(a, b))

@app.route("/luSimple",methods=['POST'])
def luSimp():
    data = request.json
    a = data["a"]
    b = data["b"]
    return dict(luSimple(a, b))

@app.route("/luPivot",methods=['POST'])
def luPiv():
    data = request.json
    a = data["a"]
    b = data["b"]
    return dict(luPivot(a, b))

# Crout needs repairings

@app.route("/jacobi",methods=['POST'])
def jacob():
    data = request.json
    a = data["a"]
    b = data["b"]
    x = data["x"]
    tol = data["tol"]
    iters = data["iters"]
    return dict(jacobi(a, b,x,2,tol,iters))

@app.route("/gaussSeidel",methods=['POST'])
def gaussSeid():
    data = request.json
    a = data["a"]
    b = data["b"]
    x = data["x"]
    tol = data["tol"]
    iters = data["iters"]
    return dict(gaussSeidel(a, b,x,2,tol,iters))

@app.route("/sor",methods=['POST'])
def so():
    data = request.json
    a = data["a"]
    b = data["b"]
    x = data["x"]
    tol = data["tol"]
    iters = data["iters"]
    w = data["w"]
    return dict(sor(a, b,x,2,tol,iters,w))


@app.route("/newtonInter",methods=['POST'])
def newtonInter():
    data = request.json
    x = data["x"]
    y = data["y"]
    return dict(newtonInterpolation(x,y))

@app.route("/vandermonde",methods=['POST'])
def vander():
    data = request.json
    x = data["x"]
    y = data["y"]
    return dict(vandermonde(x,y))

@app.route("/lagrange",methods=['POST'])
def lagrange():
    data = request.json
    x = data["x"]
    y = data["y"]
    return dict(lagrangeInterpolation(x,y))

# Cholesky needs repairings.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug = False)