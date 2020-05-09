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

def Find_S10(A,B):
    A11,A12,A21,A22=Partition_Matrix(A)
    B11,B12,B21,B22=Partition_Matrix(B)
    S=[]
    S.append(B12 - B22)  # 1
    S.append(A11 + A12)  # 2
    S.append(A21 + A22)  # 3
    S.append(B21 - B11)  # 4
    S.append(A11 + A22)  # 5
    S.append(B11 + B22)  # 6
    S.append(A12 - A22)  # 7
    S.append(B21 + B22)  # 8
    S.append(A11 - A21)  # 9
    S.append(B11 + B12)  # 10
    return S

def Find_Products(A,B,S):
    A11, A12, A21, A22 = Partition_Matrix(A)
    B11, B12, B21, B22 = Partition_Matrix(B)
    P=[]
    P.append(np.dot(A11, S[0]))
    P.append(np.dot(S[1], B22))
    P.append(np.dot(S[2], B11))
    P.append(np.dot(A22, S[3]))
    P.append(np.dot(S[4], S[5]))
    P.append(np.dot(S[6], S[7]))
    P.append(np.dot(S[8], S[9]))
    return P

def Find_Product_Terms(P):
    C11=P[4]+P[3]-P[1]+P[5]
    C12=P[0]+P[1]
    C21=P[2]+P[3]
    C22=P[4]+P[0]-P[2]-P[6]
    return (C11,C12,C21,C22)

# Driver Code
A=np.asarray([[2,3],[1,4]])
B=np.asarray([[3,7],[5,2]])
S=Find_S10(A,B)
P=Find_Products(A,B,S)
C=Find_Product_Terms(P)
# formating for display purpose
C=np.reshape(C,(2,2))
print(C)