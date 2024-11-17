"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from collections import defaultdict,Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        numsCounter = defaultdict(list)
        values = counter.values()
        values.sort()
        l = []
        for n in counter:
            numsCounter[counter[n]].append(n)
        for i in range(len(values)):
            num = values[len(values)-1-i]
            for n in numsCounter[num]:
                if k > 0:
                    l.append(n)
                else:
                    return l
        return l
