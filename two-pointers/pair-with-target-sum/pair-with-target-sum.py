"""

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

Time complexity: O(N), where ‘N’ is the total number of elements in the given array.
Space complexity: O(1)

"""
def pair_with_targetsum(arr, target_sum):
    left_ptr, right_ptr = 0, len(arr) - 1
    while (left_ptr < right_ptr):
        current_sum  = arr[left_ptr] + arr[right_ptr]
        if current_sum > target_sum:
            right_ptr -= 1
        elif current_sum == target_sum:
            return [left_ptr, right_ptr]
        else:
            left_ptr += 1
    return [1, -1]

print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11], 11))
