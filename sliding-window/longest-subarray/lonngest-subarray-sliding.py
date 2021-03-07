"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

Time complexity = O(n)
space complexity = O(1)

"""
def length_of_longest_substring(arr, k):
    max_length, max_repeat, startEle = 0, 0, 0
    num_freq = {}
    for i in range(len(arr)):
        if arr[i] == 1:
            max_repeat += 1
        if i - startEle + 1 - max_repeat > k:
            if arr[startEle] == 1:
                max_repeat -= 1
            startEle += 1
        max_length = max(max_length, i - startEle + 1)
    return max_length


array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3
print(length_of_longest_substring(array, k))
