"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals
in the input.
"""

class Solution: # space complexity : O(n) time complexity : O(nlogn)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x : x[0]) # sort by start of each interval asc
        modified_intervals = []
        for interval in intervals: # loop through the intervals
            if not modified_intervals: # if modified intervals is empty , append
                modified_intervals.append(interval)
            else:
                if interval[0] <= modified_intervals[-1][1]: # check maximum end time of interval
                    modified_intervals[-1][1] = max(interval[1],modified_intervals[-1][1])
                else: # if interval start time is larger than end of last modified, append new interval
                    modified_intervals.append(interval)
        return modified_intervals
