"""
You are given an array prices where prices[i] is the price
of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # basically we hold the smallest number we encountered so far
        # in addition we hold the largest sub we calculated , if we found smaller number
        # we replace the smallest , otherwise we check if new max sub was found.
        # finally we return the largest sub we found , time complex O(n) , space O(1)
        if len(prices)==1:
            return 0
        start = prices[0]
        max_profit = 0
        for i in range (1,len(prices)):
            if prices[i] < start:
                start = prices[i]
            else:
                max_profit = max(max_profit,prices[i]-start)

        return max_profit
