"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

Time complexity: O(nk)

"""
def sum_subarray(arr, count, sum_arr, start):
    if start+count <= len(arr):
      sum_arr.append(sum(arr[start:start+count]))
      sum_subarray(arr, count, sum_arr, start+1)
    return max(sum_arr)


arr = [2, 1, 5, 1, 3, 2]
count = 3
sum_arr = []
print(sum_subarray(arr, count, sum_arr, 0))
