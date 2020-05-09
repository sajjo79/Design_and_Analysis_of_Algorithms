import numpy as np
def Partition_Matrix(A):
    # we assume that we have squared matrix
    # that has size=power of 2, i.e. 2,4,8,16,...
    row,col=A.shape
    n=row
    half_n=n//2
    A11=A[0:half_n,0:half_n]
    A12=A[0:half_n,half_n:n]
    A21=A[half_n:n,0:half_n]
    A22=A[half_n:n,half_n:n]
    #print(A11,A12,A21,A22)
    return A11,A12,A21,A22

def Square_Matrix_Multiply_Recursive(A,B):
    C=np.zeros((A.shape))
    row,col=A.shape
    if row==1 and col==1:
        C[0,0]=A[0,0]*B[0,0]
        return C
    else:
        A11, A12, A21, A22 = Partition_Matrix(A)
        B11, B12, B21, B22 = Partition_Matrix(B)
        C11, C12, C21, C22 = Partition_Matrix(C)
        C11 = Square_Matrix_Multiply_Recursive(A11, B11) + \
              Square_Matrix_Multiply_Recursive(A12, B21)
        C12 = Square_Matrix_Multiply_Recursive(A11, B12) + \
              Square_Matrix_Multiply_Recursive(A12, B22)
        C21 = Square_Matrix_Multiply_Recursive(A21, B11) + \
              Square_Matrix_Multiply_Recursive(A22, B21)
        C22 = Square_Matrix_Multiply_Recursive(A21, B12) + \
              Square_Matrix_Multiply_Recursive(A22, B22)
        C=np.asanyarray([[C11[0][0],C12[0][0]],[C21[0][0],C22[0][0]]])
        return C

#A=np.asarray([[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,0]])
#Partition_Matrix(A)
# Driver Code
A=np.asarray([[2,3],[1,4]])
B=np.asarray([[3,7],[5,2]])
C=Square_Matrix_Multiply_Recursive(A,B)
print(C)
