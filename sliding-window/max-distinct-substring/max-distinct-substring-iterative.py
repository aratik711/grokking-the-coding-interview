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

Time complexity O(n*n)

"""
def longest_substring_with_k_distinct(str, k):
    str_count = []
    for i in range(len(str)):
        char_arr = [str[i]]
        char_count = 1
        for j in range(i+1, len(str)):
            char_count += 1
            if len(char_arr) == k:
                str_count.append(char_count)
                break
            if str[j] not in char_arr:
                char_arr.append(str[j])
                continue
    return max(str_count)

str = "cbbebi"
K = 3
print(longest_substring_with_k_distinct(str, K))
