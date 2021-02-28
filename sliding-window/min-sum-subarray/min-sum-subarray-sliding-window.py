"""

Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

time complexity = O(n+n)

"""
import math
def smallest_subarray_with_given_sum(s, arr):
    min_length = math.inf
    curr_sum = 0
    startEle = 0
    j = 1
    for i in range(len(arr)):
        if s <= arr[i]:
            return 1
        curr_sum += arr[i]
        while curr_sum >= s:
            j += 1
            min_length = min(min_length, i - startEle + 1)
            curr_sum -= arr[startEle]
            startEle += 1
    if min_length == math.inf:
        return 0
    return min_length


arr = [7, 1, 5, 2, 3, 2]
s = 7
print(smallest_subarray_with_given_sum(s,arr))
