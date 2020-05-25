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

from flask_cors import CORS, cross_origin

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
    try:
        f = data["f"]
        f = defFunction(f,"f")
    except:
        return  {"error" : True, "source" : "function definition"}
    try:
        method = dict(incrementalSearch(start,step,end))
        return { "f" : f, "method" : method}
    except:
        return {"error": True, "source": "method or function evaluation"}

@app.route("/bisection",methods=['POST'])
def bisect():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        f = data["f"]
        f = defFunction(f,"f")
    except:
        return  {"error" : True, "source" : "function definition"}
    try:
        method = dict(bisection(a,b,tol,iters))
        status = method["error"]
        return {"f": f, "method": method, "error" : status}
    except:
        return {"error": True, "source": "method or function evaluation"}

@app.route("/falseRule",methods=['POST'])
def falRule():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        f = data["f"]
        f = defFunction(f,"f")
    except:
        return {"error": True, "source": "function definition"}
    try:
        method = falseRule(a,b,tol,iters)
        status = method["error"]
        return {"f": f, "method": method, "error" : status}
    except:
        return {"error": True, "source": "method or function evaluation"}

@app.route("/newton",methods=['POST'])
def newt():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        f = data["f"]
        f = defFunction(f,"f")
        df = data["df"]
        df = defFunction(df,"df")
    except:
        return {"error": True, "source": "function definition"}
    try:
        method = dict(newton(a,tol,iters))
        status = method["error"]
        return  {"f": f, "df": df, "method": method, "error" : status}
    except:
        return {"error": True, "source": "method or function evaluation"}

@app.route("/fixedPoint",methods=['POST'])
def fixPoint():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        f = data["f"]
        f = defFunction(f, "f")
        g = data["g"]
        g = defFunction(g, "g")
    except:
        return {"error": True, "source": "function definition"}
    try:
        method = dict(fixedPoint(a,tol,iters))
        status = method["error"]
        return {"f": f, "g": g, "method": method, "error" : status}
    except:
        return {"error": True, "source": "method or function evaluation"}


@app.route("/secant",methods=['POST'])
def seca():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        f = data["f"]
        f = defFunction(f, "f")
    except:
        return {"error": True, "source": "function definition"}
    try:
        method =  dict(secant(a,b,tol,iters))
        status = method["error"]
        return {"f": f, "method": method, "error" : status}
    except:
        return {"error": True, "source": "method or function evaluation"}

@app.route("/multipleRoots",methods=['POST'])
def multiRoot():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        f = data["f"]
        f = defFunction(f, "f")
        df = data["df"]
        df = defFunction(df,"df")
        ddf = data["ddf"]
        ddf = defFunction(ddf,"ddf")
    except:
        return {"error": True, "source": "function definition"}
    try:
        method = dict(multipleRoots(a,tol,iters))
        status = method["error"]
        return {"f" : f, "df" : df, "ddf" : ddf, "method" : method, "error" : status}
    except:
        return {"error": True, "source": "method or function evaluation"}

@app.route("/gaussSimple",methods=['POST'])
def gaussSimp():
    data = request.json
    a = data["a"]
    b = data["b"]
    try:
        return dict(gaussSimple(a,b))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/gaussPartial",methods=['POST'])
def gaussPart():

    data = request.json
    a = data["a"]
    b = data["b"]
    try:
        return dict(partialPivot(a, b))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/gaussTotal",methods=['POST'])
def gaussTot():
    data = request.json

    a = data["a"]
    b = data["b"]
    try:
        return dict(gaussTotal(a, b))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/luSimple",methods=['POST'])
def luSimp():
    data = request.json
    a = data["a"]
    b = data["b"]
    try:
        return dict(luSimple(a, b))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/luPivot",methods=['POST'])
def luPiv():
    data = request.json
    a = data["a"]
    b = data["b"]
    try:
        return dict(luPivot(a, b))
    except:
        return {"error": True, "source": "method evaluation"}

# Crout needs repairings

@app.route("/jacobi",methods=['POST'])
def jacob():
    data = request.json
    a = data["a"]
    b = data["b"]
    x = data["x"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        return dict(jacobi(a, b,x,2,tol,iters))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/gaussSeidel",methods=['POST'])
def gaussSeid():
    data = request.json
    a = data["a"]
    b = data["b"]
    x = data["x"]
    tol = data["tol"]
    iters = data["iters"]
    try:
        return dict(gaussSeidel(a, b,x,2,tol,iters))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/sor",methods=['POST'])
def so():
    data = request.json
    a = data["a"]
    b = data["b"]
    x = data["x"]
    tol = data["tol"]
    iters = data["iters"]
    w = data["w"]
    try:
        return dict(sor(a, b,x,2,tol,iters,w))
    except:
        return {"error": True, "source": "method evaluation"}


@app.route("/newtonInter",methods=['POST'])
def newtonInter():
    data = request.json
    x = data["x"]
    y = data["y"]
    try:
        return dict(newtonInterpolation(x,y))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/vandermonde",methods=['POST'])
def vander():
    data = request.json
    x = data["x"]
    y = data["y"]
    try:
        return dict(vandermonde(x,y))
    except:
        return {"error": True, "source": "method evaluation"}

@app.route("/lagrange",methods=['POST'])
def lagrange():
    data = request.json
    x = data["x"]
    y = data["y"]
    try:
        return dict(lagrangeInterpolation(x,y))
    except:
        return {"error": True, "source": "method evaluation"}

# Cholesky needs repairings.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug = False)
  cors = CORS(app)