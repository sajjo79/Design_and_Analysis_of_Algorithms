def Quick_Sort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quick_Sort(A, p, q-1)
        Quick_Sort(A, q+1, r)

def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)

 # Driver code
A = [2, 8, 7, 1, 3, 5, 6, 4]
p = 0
r = len(A)
Quick_Sort(A, p, r-1)
print("Array after quick sort..:")
print(A)
