'''
Q.  Given an array of positive integers arr[], return the second largest 
    element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
'''

arr = [2,5,33,65,96,90,88,96,90]
# arr = [ 5 ]

def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    first = second = -1

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second

print(second_largest(arr))