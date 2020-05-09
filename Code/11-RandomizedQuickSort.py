# The algorithm is code by
# Ishtiaq Ahmed - MSCS ISP Multan
def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)

def Randomized_Partition(A,p,r):
    from random import randint
    i = randint(p, r)
    A[i],A[r]=A[r],A[i]
    q = Partition(A,p,r)
    return q

def Randomized_Quick_Sort(A, p, r):
    if p < r:
        q = Randomized_Partition(A, p, r)
        Randomized_Quick_Sort(A, p, q-1)
        Randomized_Quick_Sort(A, q+1, r)

# Driver code
A = [2, 8, 7, 1, 3, 5, 20, 4,10,9,6]
p = 0
r = len(A)
Randomized_Quick_Sort(A, p, r-1)
print("Array after quick sort..:")
print(A)
