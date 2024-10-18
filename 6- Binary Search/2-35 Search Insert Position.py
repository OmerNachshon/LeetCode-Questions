"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = right//2
        while nums[mid] != target and left<right:
            if nums[mid] < target:
                left = min(mid+1,len(nums)-1)
            else:
                right = max(mid-1,0)
            mid = (right+left)//2
        if nums[mid]==target:
            return mid
        if target > nums[mid]:
            return mid+1
        return mid
