"""

Given a string, find the length of the longest substring, which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

Time complexity = O(n)

"""
def non_repeat_substring(string):
    startEle = 0
    char_seen = []
    max_length = 0
    for i in range(len(string)):
        if string[i] in char_seen:
            char_seen = []
            startEle = i
        char_seen.append(string[i])
        max_length = max(max_length, i-startEle+1)
    return max_length

string="abcabcd"
print(non_repeat_substring(string))
