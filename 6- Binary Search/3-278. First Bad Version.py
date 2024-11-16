"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        good_versions = set()
        bad_versions = set()
        l ,r = 1 , n
        while l <= r:
            mid = (r+l) // 2
            res = isBadVersion(mid)
            if res:
                bad_versions.add(mid)
                if mid == 0 or mid-1 in good_versions:
                    return mid
                r=mid-1
            else:
                good_versions.add(mid)
                if mid+1 in bad_versions or mid+1 == n:
                    return mid+1
                l=mid+1
        return 1
