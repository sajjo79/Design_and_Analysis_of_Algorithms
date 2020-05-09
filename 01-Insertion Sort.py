def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        print(A)

A = [5,2,4,6,1,3]
insertionSort(A)
print("Sorted array is:", A)
