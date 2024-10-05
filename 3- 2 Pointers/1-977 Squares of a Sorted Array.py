"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in
non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        left  = 0
        right = len(nums)-1
        index = len(nums)-1
        while right >= left:
            if nums[left]**2 >= nums[right]**2:
                arr[index] = nums[left]**2
                left+=1
            else:
                arr[index] = nums[right]**2
                right-=1
            index-=1
        return arr
