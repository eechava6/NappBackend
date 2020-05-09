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
from template import template
from LUpivot import luPivot
from LUsimple import luSimple
from crout import crout
from flask import Flask 

app = Flask(__name__)

@app.route("/IS")
def inc():
    return str(incrementalSearch(0,0.1,1))

    
if __name__ == "__main__":
    app.run(debug=True)