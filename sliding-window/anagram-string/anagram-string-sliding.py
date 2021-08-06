"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

Time complexity: O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively
space complexitiy: O(M)

"""
def find_string_anagrams(str, pattern):
  result_indexes = []
  window_start, matched = 0, 0
  char_freq = {}
  for chr in pattern:
      if chr not in char_freq:
        char_freq[chr] == 0
      char_freq[chr] += 1
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_freq:
      char_freq[right_char] -= 1
      if char_freq[right_char] == 0:
        matched += 1
    if matched == len(char_freq):
        result_indexes.append(window_start)
    if window_end > len(pattern) - 1:
        left_char = str[window_start]
        window_start += 1
        if left_char in char_freq:
            if char_freq[left_char] == 0:
                matched -= 1
            char_freq[left_char] += 1
  return result_indexes

print(find_string_anagrams("ppqp", "pq"))
print(find_string_anagrams("abbcabc", "abc"))



  return result_indexes
