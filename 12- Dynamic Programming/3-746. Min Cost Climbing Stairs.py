"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost[0],cost[1])
        dp = [0] * (len(cost)+1)
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[-1]
