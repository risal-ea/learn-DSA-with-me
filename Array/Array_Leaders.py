'''
Q.You are given an array arr of positive integers. Your task is to find all the 
leaders in the array. An element is considered a leader if it is greater than or equal 
to all elements to its right. The rightmost element is always a leader.

Examples:

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

Input: arr = [30, 10, 10, 5]
Output: [30, 10, 10, 5]
Explanation: When an array is sorted in non-increasing order, all elements are leaders.
'''

arr = [ 16, 17, 4, 3, 5, 2 ]

def find_leader(arr):
    leaders = []
    n = len(arr)
    max_right_no = arr[-1]
    leaders.append(max_right_no)

    for i in range(n-2, -1, -1):
        if arr[i] >= max_right_no:
            max_right_no = arr[i]
            leaders.append(arr[i])

    leaders.reverse()
    return leaders

print(find_leader(arr))
