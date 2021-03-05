"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Time complexity O(n+n) = O(n)
space complexity O(k)

"""
def longest_substring_with_k_distinct(str, k):
    max_length = 0
    startEle = 0
    char_freq = {}
    for i in range(len(str)):
        right_char = str[i]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while len(char_freq) > k:
            left_char = str[startEle]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            startEle += 1
        max_length = max(max_length,i-startEle+1)
    return max_length




    return max(str_count)

str = "cbbebi"
K = 3
print(longest_substring_with_k_distinct(str, K))
