"""
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].

Time complexity: O(N), where ‘N’ is the total number of elements in the given array.
Space complexity: O(1)

"""
def remove_element(arr, key):
    count = 0
    for i in range(len(arr)):
        if arr[i] != key:
            count += 1
    return count


print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))
