'''
Q: You are given an array arr[] of size n - 1 that contains distinct integers 
in the range from 1 to n (inclusive). This array represents a permutation of the 
integers from 1 to n with one element missing. Your task is to identify and return 
the missing element. 
'''

arr = [1, 2, 3, 5]

def finding_missing_number(arr):
    n = len(arr) + 1
    sumTotal = n * (n + 1) // 2
    arraySum = sum(arr)
    print(sumTotal - arraySum)

finding_missing_number(arr)