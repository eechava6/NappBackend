import json
from math import sqrt
 
def cholesky(matrix_A):
    n = len(matrix_A)
    L = [[0.0] * n for _ in range(len(matrix_A))]
    for i in range(len(matrix_A)):
        for k in range(i+1):
            suma = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k):
                L[i][k] = sqrt(matrix_A[i][i] - suma)
            else:
                L[i][k] = (1.0 / L[k][k] * (matrix_A[i][k] - suma))
  
    return L

print()
matrix_A = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
L = cholesky(matrix_A)
result = "matrix = { 'L': " + str(L) + " }"
print(result)



