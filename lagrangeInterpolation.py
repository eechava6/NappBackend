import numpy as np

x = np.array([-1, 0, 3, 4])
y = np.array([15.5, 3, 8, 1])

nx = len(x)
ny = len(y)

Li = []

# fill the y[i]*L[i]x
for xi in range(nx):
    Li.append({"numerator": "", "multiplier": 0, "multiplier2": 0})
    auxMultiplier = 1
    for xi2 in range(nx):
        if (xi != xi2):
            auxNumerator = -1 * x[xi2]
            if (auxNumerator >= 0):
                auxNumerator = "+" + str(auxNumerator)
            else:
                auxNumerator = str(auxNumerator)
            Li[xi]['numerator'] += "(x" + auxNumerator + ")"

            auxMultiplier *= x[xi] - x[xi2]

    Li[xi]['multiplier'] = 1 / auxMultiplier
    Li[xi]['multiplier2'] = y[xi] * (1 / auxMultiplier)

Li.append({"result": ""})
result = ""

for i in range(0, len(Li) - 1):
    if (Li[i]["multiplier"] >= 0):
        Li[len(Li) - 1]["result"] += "+"

    Li[len(Li) - 1]["result"] += str(Li[i]['multiplier2']) + "*" + Li[i]['numerator']
    print("L", i, "= ", Li[i]['multiplier'], "*", Li[i]['numerator'])

print("Result=", Li[len(Li) - 1]["result"])
