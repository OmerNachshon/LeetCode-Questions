"""
Given a string s, find the length of the longest
substring
 without repeating characters.

"""
from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hashmap = OrderedDict()
        temp = 0
        remove = []
        for i,val in enumerate(s):
            if val in hashmap:
                longest = max(longest,temp)
                for key in hashmap:
                    remove.append(key)
                    temp-=1
                    if key == val:
                        break
                for r in remove:
                    del hashmap[r]
                remove.clear()
            hashmap[val] = i
            temp+=1
        return max(longest,temp)


