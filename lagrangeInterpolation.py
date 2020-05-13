import numpy as np
import sympy as sym

x = np.array([-2, -1, 2, 3])
y = np.array([12.13533528, 6.367879441, -4.610943901, 2.085536923])

print(x)
print(y)

nx = len(x)
ny = len(y)

Li = []

count = 0
print("y(x)*Li(x):")
# fill the y[i]*L[i]x
for xi in range(nx):
    Li.append({"numerator":"", "multiplier":0})
    auxMultiplier = 1
    for xi2 in range(nx):
        if(xi != xi2):
            auxNumerator = -1*x[xi2]
            if(auxNumerator > 0):
                auxNumerator = "+"+str(auxNumerator)
            else:
                auxNumerator = str(auxNumerator)
            Li[xi]['numerator'] += "(x"+auxNumerator+")"
            
            auxMultiplier *= x[xi]-x[xi2]
    
    Li[xi]['multiplier'] = y[xi]*(1/auxMultiplier)


Li.append({"result":""})
result = ""

for i in range(0,len(Li)-1):
    if(Li[i]["multiplier"]  > 0):
        Li[len(Li)-1]["result"] += "+"    

    Li[len(Li)-1]["result"] += str(Li[i]['multiplier'])+"*"+Li[i]['numerator']
    print("L", i, "= ", Li[i]['multiplier'],"*",Li[i]['numerator'])

print("Result=", Li[len(Li)-1]["result"])
