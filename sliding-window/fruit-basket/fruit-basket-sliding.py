"""
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

Time complexity: O(n)

"""
def fruits_into_baskets(fruits):
    max_length = 0
    startEle = 0
    baskets = {}
    for i in range(len(fruits)):
        if fruits[i] not in baskets:
            baskets[fruits[i]] = 0
        baskets[fruits[i]] += 1
        while len(baskets) > 2:
            baskets[fruits[startEle]] -= 1
            if baskets[fruits[startEle]] == 0:
                del baskets[fruits[startEle]]
            startEle += 1
        max_length = max(max_length, i-startEle+1)
    return max_length


fruits=['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits))
