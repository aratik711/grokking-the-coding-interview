"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

Time complexity: O(N*logN+sq(N)) ~ O(2*sq(N)) ~ O(sq(N))
Space complexity: O(N)

"""
def search_triplets(arr):
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        find_pair(arr, -arr[i], i+1, triplets)
    return triplets

def find_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if target_sum == current_sum:
            triplets.append([-current_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))
