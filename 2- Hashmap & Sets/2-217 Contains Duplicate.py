"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False
