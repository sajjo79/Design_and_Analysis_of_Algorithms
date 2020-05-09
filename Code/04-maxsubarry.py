
def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -10000
    sum = 0;
    max_left,max_right=0,0
    for i in range(mid, low , -1):
        sum = sum + A[i]
        if (sum > left_sum):
            left_sum = sum
            max_left=i

    right_sum = -1000
    sum = 0;
    for j in range(mid + 1, high):
        sum = sum + A[j]
        if (sum > right_sum):
            right_sum = sum
            max_right=j

    return max_left,max_right,max(left_sum + right_sum, left_sum, right_sum)


def find_maximum_subarray(A, low, high):
    # Base Case: Only one element 
    if (low == high):
        return low,high,A[low]

    mid = (low + high) // 2
    left_low,left_high,left_sum=find_maximum_subarray(A, low, mid)
    right_low,right_high,right_sum=find_maximum_subarray(A, mid + 1, high)
    cross_low,cross_high,cross_sum=find_max_crossing_subarray(A, low, mid, high)
    if(left_sum>=right_sum and left_sum>=cross_sum):
        return left_low,left_high,left_sum
    elif (right_sum>=left_sum and right_sum>=cross_sum):
        return right_low,right_high,right_sum
    else:
        print(cross_low,cross_high,cross_sum)
        return cross_low,cross_high,cross_sum

# Driver Code
#     0   1  2  3   4   5  6  7  8  9  10  11 12 13 14 15
A = [-13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
n = len(A)

low,high,max_sum = find_maximum_subarray(A, 0, n - 1)
print("Maximum contiguous sum is ", low+1,high+1,max_sum)

