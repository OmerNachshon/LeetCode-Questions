"""
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_dist = 0
        num_zeros = 0
        n = len(nums)
        start = 0

        for end in range(n):
            if nums[end] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[start] == 0:
                    num_zeros -= 1
                start += 1
            dist = end - start + 1
            max_dist = max(max_dist, dist)

        return max_dist

