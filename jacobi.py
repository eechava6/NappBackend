import numpy as np

def jacobi(A, b, x, norm, tol, iteMax):
    result = {}
    iters = []
    D = np.diag(np.diag(A))
    L = (-1 * np.tril(A))+D
    U = (-1 * np.triu(A))+D
    if(0 in np.diag(A)): return {"status" : "diagonal has 0"}
    ite = 0
    #Change here for Jacobi, Sor and Gauss seidel
    T = np.dot(np.linalg.inv(D), (L+U))
    C = np.dot(np.linalg.inv(D),b)
    #End changes
    spectRad = np.max(np.absolute(np.linalg.eigvals(T)))
    if(spectRad > 1): return {"status" : "spectral radious > 1"}
    #Saving into result dict
    result['TMatrix'] = T
    result['CMatrix'] = C
    result['SpectRad'] = spectRad
    iters.append({ "iter" : ite, "E" : "n/a", "x" : x })
    #End savings
    while(norm > tol and ite < iteMax):
        xold = x
        x = np.dot(T,xold)+C
        norm = np.linalg.norm(xold-x)
        ite += 1
        #Saving into iters
        iters.append({ "iter" : ite,  "E" : norm,  "x" : x})
        #End saving
    result['Iters'] = iters
    return result
