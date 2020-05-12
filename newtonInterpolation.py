import numpy as np

x = np.array([1,1.2,1.4,1.6,1.8,2]) # x coordinates in space
y = np.array([0.6747,0.8491,1.1214,1.4921,1.9607,2.5258]) # f(x)

n = len(y)

print("x: ")
print(x)
table = np.zeros([n, n]) # Create a square matrix to hold table
table[::,0] = y # first column is y
print("y:")
print(y)

results={"table":[], "coefficient": []}

def getCoeffs(x, y):
    """ Creates Newton table and extracts coefficients """
    for j in range(1,n):
        results["table"].append([])
        for i in range(n-j):
            # create table by updating other columns
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])
            results["table"][len(results["table"])-1].append(table[i][j])
    
    coeff = table[0] # return first row
    for c in coeff:
        results["coefficient"].append(c)

    index = 1
    for i in results["table"]:
        print("Column ",index)
        print(i)
        index += 1

    return table[0]

coeff_vector = getCoeffs(x, y)


print("The newton polynom is: ")
for i in range(n):
    print(coeff_vector[i],end=" ")
    for j in range(i):
        print("( x -",x[j],")",end=" ")
    if(i != n-1):
        print("+",end=" ")
print()


