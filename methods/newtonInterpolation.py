import numpy as np
import ast

def newtonInterpolation(x, y):
    x = ast.literal_eval(x)
    y = ast.literal_eval(y)
    n = len(y)
    table = np.zeros([n, n])  # Create a square matrix to hold table
    table[::, 0] = y  # first column is y

    results = {"table": [], "coefficient": []}
    results["table"].append(y)
    """ Creates Newton table and extracts coefficients """
    for j in range(1, n):
        column = []
        for i in range(j):
            column.append(0)
        for i in range(n - j):
            # create table by updating other columns
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
            column.append( table[i][j])
        results["table"].append(column)


    coeff = table[0]  # return first row
    for c in coeff:
        results["coefficient"].append(c)
    polynom = ""
    for i in range(n):
        polynom += str(round(table[0][i],4))
        for j in range(i):
            polynom+= "*( x -"+ str(round(x[j],4))+ ")"
        if (i != n - 1):
            polynom += "+"
    polynom = polynom.replace(" ", "").replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-")
    results["polynom"] = polynom
    return results



