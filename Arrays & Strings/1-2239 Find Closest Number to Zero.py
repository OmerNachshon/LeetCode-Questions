"""
Given an integer array nums of size n,
return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.
"""

import math
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_distance = math.pow(10,5)+1
        for num in nums:
            if abs(num) == abs(min_distance) and min_distance>num:
                continue
            if abs(num) <= abs(min_distance):
                min_distance = num

        return min_distance
