"""
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = []
        for ch in s:
            if ch.isalnum():
                new_s.append(ch)
        s = "".join(new_s)
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True
