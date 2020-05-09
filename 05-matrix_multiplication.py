import numpy as np
def multiply_matrices(A,B):
    row,col=A.shape
    C=np.zeros((A.shape))
    for i in range(row):
        for j in range(col):
            C[i,j]=0
            for k in range(col):
                C[i,j]=C[i,j]+A[i,k]*B[k,j]
    return C

A=np.asarray([[2,3],[1, 4]])
B=np.asarray([[3,7],[5,2]])
C=multiply_matrices(A,B)
print(C)
print(np.dot(A,B))