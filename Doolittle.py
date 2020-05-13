import numpy as np
import json
                                    
def lower(matrix):
    error=0
    for z in range (matrix-1):
        for x in range(1, matrix):
            if (z < x ):
                matrix_B[x][z]=mult[error]
                error=error+1
                    
def higher(matrix):
    print("Result = {",end="")
    
    print("'HigherU': ",end="")
    for i in range (matrix):
            print (matrix_A[i][:],end="")
    print(",",end="")
def lower1(matrix):
    print()
    print("'lowerL':",end="")
    for i in range (matrix):
            print (matrix_B[i][:],end="")
    print("}",end="")
def gauss(matrix):
    error=0 
    for z in range (matrix-1):
        for x in range(1, matrix-z):
            if (matrix_A[z][z] != 0 ):
                p = matrix_A[x+z][z] / matrix_A[z][z]
                mult[error]=-1*p
                error=error+1
                for y in range (matrix):
                    matrix_A[x+z][y] = matrix_A[x+z][y] - (matrix_A[z][y]*p)           

if __name__ == "__main__":
    matrix=3
    matrix_A = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
    matrix_B= [[1,0,0],[0,1,0],[0,0,1],] 
    mult=np.zeros(matrix)
    
    lower(matrix)
    higher(matrix)
    lower1(matrix)
    gauss(matrix)