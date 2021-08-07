"""
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

Time Complexity: O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively
Space complexity: O(N)

"""
def find_substring(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_freq = {}

    for chr in pattern:
        if chr not in char_freq:
            char_freq[chr] = 0
        char_freq[chr] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] >= 0:
                matched += 1
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1
    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start+min_length]



print(find_substring("aabdec", "abc"))
print(find_substring("abdbca", "abc"))
print(find_substring("adcad", "abc"))
