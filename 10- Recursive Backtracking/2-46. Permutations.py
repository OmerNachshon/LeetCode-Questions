"""
Given an array nums of distinct integers, return all the possible
permutations
. You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def permuteHelper(nums,curr):
            if not nums:
                permutations.append(curr)
                return
            for i in range(len(nums)):
                permuteHelper(nums[0:i]+nums[i+1:],[*curr,nums[i]])

        permuteHelper(nums,[])
        return permutations
