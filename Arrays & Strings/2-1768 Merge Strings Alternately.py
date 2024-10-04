"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order,
starting with word1.
If a string is longer than the other,
append the additional letters onto the end of the merged string.
Return the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = []
        for i in range (min(len(word1),len(word2))):
            new_word.append(word1[i])
            new_word.append(word2[i])
        if len(word1) == len(word2):
            return "".join(new_word)
        elif len(word1) > len(word2):
            return "".join(new_word)+word1[len(word2):]
        else:
            return "".join(new_word)+word2[len(word1):]
