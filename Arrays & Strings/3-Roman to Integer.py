"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        final_val = 0
        for i in range(len(s)):
            if i+1 < len(s) and hmap[s[i]] < hmap[s[i+1]]:
                final_val -= hmap[s[i]]
            else:
                final_val += hmap[s[i]]
        return final_val
