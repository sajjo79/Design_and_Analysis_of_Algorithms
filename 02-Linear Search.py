def Linear_Search(Arr,x):
    for i in range(len(Arr)):
        if Arr[i]== x:
            return i
    return -1

Arr=[0,1,2,3,4,5,6,7,8,9]
loc=Linear_Search(Arr,8)
if loc>-1:
    print("The search element is present at ",loc)
else:
    print("The element is not present in the array")