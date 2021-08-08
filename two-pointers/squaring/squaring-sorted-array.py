"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

Time complexity: O(N)
Space complexity: O(N)

"""
def make_squares(arr):
    squares = [0 for i in range(len(arr))]
    left, right = 0, len(arr)-1
    highestSquareIndex = len(arr)-1
    while left <= right:
        leftSq = arr[left] * arr[left]
        rightSq = arr[right] * arr[right]
        if leftSq > rightSq:
            squares[highestSquareIndex] = leftSq
            left += 1
        else:
            squares[highestSquareIndex] = rightSq
            right -= 1
        highestSquareIndex -= 1
    return squares

print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
