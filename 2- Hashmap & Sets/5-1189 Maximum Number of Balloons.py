"""
Given a string text, you want to use the characters of
text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter_hashset = Counter(text)
        # for 1 balloon , we need b:1 a:1 l:2 o:2 n:1
        n = min([counter_hashset['b'],counter_hashset['a'],counter_hashset['n']]) * 2
        return min([n,counter_hashset['o'],counter_hashset['l']])//2
