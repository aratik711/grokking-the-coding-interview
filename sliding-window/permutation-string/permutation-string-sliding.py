"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

Time complexity: O(N+M), where ‘N’ and ‘M’ are the number of characters in the input string and the pattern
space complexity: O(M)
"""
def find_permutation(str, pattern):
    window_start, matched = 0, 0
    char_freq = {}

    for chr in pattern:
        if chr not in char_freq:
            char_freq[chr] = 0
        char_freq[chr] += 1

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        if matched == len(char_freq):
            return True

        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1
    return False

print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))
