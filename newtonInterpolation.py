import numpy as np

x = np.array([-1, 1, 2.569858113, 6])  # x coordinates in space
y = np.array([1, 3, 1, -2])  # f(x)

def newtonInterpolation(x, y):
    n = len(y)
    table = np.zeros([n, n])  # Create a square matrix to hold table
    table[::, 0] = y  # first column is y

    results = {"table": [], "coefficient": []}
    """ Creates Newton table and extracts coefficients """
    for j in range(1, n):
        column = []
        for i in range(n - j):
            # create table by updating other columns
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
            column.append( table[i][j])
        results["table"].append({"column" : column, "index" : j})

    coeff = table[0]  # return first row
    for c in coeff:
        results["coefficient"].append(c)

    for i in range(n):
        print(table[0][i], end=" ")
        for j in range(i):
            print("( x -", x[j], ")", end=" ")
        if (i != n - 1):
            print("+", end=" ")
    print()

    return results


coeff_vector = newtonInterpolation(x, y)



