"""

Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

Time  complexity = O(n)

"""
def length_of_longest_substring(string, k):
    startEle, max_length, max_repeat = 0, 0, 0
    char_freq = {}
    for i in range(len(string)):
        if string[i] not in char_freq:
            char_freq[string[i]] = 0
        char_freq[string[i]] += 1
        max_repeat = max(max_repeat, char_freq[string[i]])
        if i - startEle + 1 - max_repeat > k:
            char_freq[string[startEle]] -= 1
            startEle += 1
        max_length = max(max_length,i - startEle + 1)
    return max_length


string="abbcb"
k = 2
print(length_of_longest_substring(string, k))
