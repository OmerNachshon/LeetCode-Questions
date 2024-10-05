"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [str(nums[0])]
        start = nums[0]
        return_l = []
        for i in range (1,len(nums)):
            val = nums[i]
            if val != nums[i-1] + 1:
                if nums[i-1] == start:
                    return_l.append(str(start))
                else:
                    return_l.append(str(start)+"->"+str(nums[i-1]))
                start = val
        if start == nums[-1]: # last num wasn't consecutive
            return_l.append(str(start))
        else:
            return_l.append(str(start)+"->"+str(nums[-1]))
        return return_l


