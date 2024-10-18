"""
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        for i in range(len(nums)):
            for j in range(len(sol)):
                sol.append(sol[j]+[nums[i]])
        return sol
