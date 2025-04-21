'''
Q. Given an array arr of integers, find all the elements that occur more than 
once in the array. If no element repeats, return an empty array.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.
'''

#Solution 1
arr = [2, 3, 1, 2, 3]

def find_duplicates(arr):
    dupes = []
    seen = []

    for num in arr:
        if num in seen and num not in dupes:
            dupes.append(num)
        else:
            seen.append(num)
    print(dupes)

find_duplicates(arr)

#More optimized solution

def find_dupe(arr):
    dupes = set()
    seen = set()

    for num in arr:
        if num in seen:
            dupes.add(num)
        else:
            seen.add(num)
    print(list(dupes))

find_dupe(arr)