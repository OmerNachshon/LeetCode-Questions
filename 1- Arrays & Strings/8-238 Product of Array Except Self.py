"""

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and
without using the division operation.

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1
            l_arr[i] = l_mult # hold current mult from left without current left val
            r_arr[j] = r_mult # hold current mult from right without current right val
            l_mult *= nums[i]
            r_mult *= nums[j]
        # return array of multiplications of total from left with total from right
        #  l is all multiplications from left without nums[i] at ith
        #  r is all multiplications from right without nums[i] at ith
        #  we return combinations of l*r
        return [l*r for l, r in zip(l_arr, r_arr)]
