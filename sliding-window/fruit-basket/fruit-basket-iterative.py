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

Time complexity: O(n*n)

"""
def fruits_into_baskets(fruits):
    length = []
    for i in range(len(fruits)):
        basket1 = {}
        basket2 = {}
        basket1[fruits[i]] = 1
        count = 1
        for j in range(i+1,len(fruits)):
            if fruits[j] in basket1:
                basket1[fruits[j]] += 1
                count += 1
            elif fruits[j] not in basket1:
                if len(basket2) == 0:
                    basket2[fruits[j]] = 1
                    count += 1
                elif fruits[j] in basket2:
                    basket2[fruits[j]] += 1
                    count += 1
            if j == len(fruits)-1:
                length.append(count)
            elif fruits[j] not in basket2 and fruits[j] not in basket1 and len(basket1) == 1 and len(basket2) == 1:
                length.append(count)
                break
    return max(length)


fruits=['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits))
