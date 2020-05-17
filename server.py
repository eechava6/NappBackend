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
from LUpivot import luPivot
from LUsimple import luSimple
from crout import crout
from gaussSeidel import gaussSeidel
from jacobi import jacobi
from sor import sor

from flask import Flask, request

app = Flask(__name__)

@app.route("/incSearch",methods=['POST'])
def incSearch():
    data = request.json
    start = data["start"]
    step = data["step"]
    end = data["end"]
    return dict(incrementalSearch(start,step,end))

@app.route("/bisection",methods=['POST'])
def bisect():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    return dict(bisection(a,b,tol,iters))

@app.route("/falseRule",methods=['POST'])
def falRule():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    return falseRule(a,b,tol,iters)

@app.route("/newton",methods=['POST'])
def newt():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    return dict(newton(a,tol,iters))

@app.route("/fixedPoint",methods=['POST'])
def fixPoint():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    return dict(fixedPoint(a,tol,iters))

@app.route("/secant",methods=['POST'])
def seca():
    data = request.json
    a = data["a"]
    b = data["b"]
    tol = data["tol"]
    iters = data["iters"]
    return dict(secant(a,b,tol,iters))

@app.route("/multipleRoots",methods=['POST'])
def multiRoot():
    data = request.json
    a = data["a"]
    tol = data["tol"]
    iters = data["iters"]
    return dict(multipleRoots(a,tol,iters))

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


if __name__ == "__main__":
    app.run(debug=True)