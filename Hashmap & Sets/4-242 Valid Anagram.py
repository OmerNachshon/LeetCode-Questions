"""
Given two strings s and t, return true if t is
an anagram of s, and false otherwise.
"""

# basically an anagram is if both have the same characters and
# the same number of each character
# so we use Counter , which creates a hashmap with characters as keys and counter of them as values
# then we can compare both counter objects and return True if equal and False otherwise
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
