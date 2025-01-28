"""
122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for idx in range(len(prices) - 1):
            maxProf += max(0, prices[idx + 1] - prices[idx])
        return maxProf

stocks = [100, 180, 260, 310, 40, 535, 695]
sl = Solution()
sl.maxProfit(stocks)