'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
'''

def multiply(arr):
    F = G = [1]*len(arr)
    for i in range(1, len(arr)):
        F[i] = arr[i-1]*F[i-1]
    for i in range(len(arr)-2, -1, -1):
        G[i] = arr[i+1]*G[i+1]

    return [x*y for x, y in zip(F, G)]