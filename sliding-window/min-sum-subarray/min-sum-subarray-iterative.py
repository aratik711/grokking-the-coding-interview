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

time complexity = O(n*n)

"""
def smallest_subarray_with_given_sum(s, arr):
    min_length = len(arr)
    for i in range(len(arr)):
        if s <= arr[i]:
            min_length = 1
            break
        curr_sum = arr[i]
        curr_length = 1
        for j in range(i+1, len(arr)):
            curr_length += 1
            if curr_length >= min_length:
                break
            curr_sum += arr[j]
            if curr_sum >= s:
                min_length = curr_length
                break
    return min_length


arr = [3, 4, 1, 1, 6]
s = 8
print(smallest_subarray_with_given_sum(s,arr))
