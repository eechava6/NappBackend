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


@app.route("/",methods=['GET'])
def hello():
    return """<h2 style="text-align: center;"><strong style="background-color: #317399; padding: 0 5px; color: #fff;">Hello! backend is working&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-embarassed.gif" alt="embarassed" /></strong></h2>
            <p style="text-align: center;"><span style="color: #000080;"><strong> available endpoints: </strong></span></p>
            <p style="text-align: center;"><br />/bisection</p>
            <p style="text-align: center;">/incSearch</p>
            <p style="text-align: center;">/falseRule</p>
            <p style="text-align: center;">/newton</p>
            <p style="text-align: center;">/fixedPoint</p>
            <p style="text-align: center;">/secant</p>
            <p style="text-align: center;">/multipleRoots</p>
            <p style="text-align: center;">/gaussSimple</p>
            <p style="text-align: center;">/gaussPartial</p>
            <p style="text-align: center;">/gaussTotal</p>
            <p style="text-align: center;">/luSimple</p>
            <p style="text-align: center;">/luPivot</p>
            <p style="text-align: center;">/jacobi</p>
            <p style="text-align: center;">/gaussSeidel</p>
            <p style="text-align: center;">/sor</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
             """

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

# Cholesky needs repairings.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug = False)