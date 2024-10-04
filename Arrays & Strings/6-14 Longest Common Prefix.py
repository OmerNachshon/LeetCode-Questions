"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        longest_prefix = ""
        min_length = min([len(word) for word in strs])
        first_word = strs[0]
        for i in range(min_length):
            if all([first_word[i] == word[i] for word in strs]):
                longest_prefix+=first_word[i]
            else:
                return longest_prefix
        return longest_prefix
