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

Time complexity: O(n)
Space complexity : O(1)

"""
def sum_subarray(arr, count):
    sum_arr = []
    curr_sum = 0.0
    startEle = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if i >= count - 1:
          sum_arr.append(curr_sum)
          curr_sum = curr_sum - arr[startEle]
          startEle += 1
    return max(sum_arr)

arr = [2, 1, 5, 1, 3, 2]
count = 3
print(sum_subarray(arr, count))
