import numpy as np
def Parent(i):
    return i//2
def Left(i):
    return 2*i
def Right(i):
    return 2*i+1
heap_size=0
largest=0

def Max_Heapify(A,i):
    l=Left(i)
    r=Right(i)
    if(l<heap_size and A[l]>A[i]):
        largest=l
    else:   largest=i
    if(r<heap_size and A[r]>A[largest]):
        largest=r
    if largest!=i:
        t=A[i]
        A[i]=A[largest]
        A[largest]=t
        Max_Heapify(A,largest)

def Build_Max_Heap(A):
    global heap_size
    heap_size=len(A)
    for i in range(len(A)//2,-1,-1):
        Max_Heapify(A,i)
    return A
# Driver Code
A=np.asarray([4,1,3,2,16,9,10,14,8,7])
print(A)
A=Build_Max_Heap(A)
print(A)



