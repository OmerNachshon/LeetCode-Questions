"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        print(magazine)
        for ch in ransomNote:
            if ch not in magazine or magazine[ch]<1:
                return False
            else:
                magazine[ch]-=1
        return True
