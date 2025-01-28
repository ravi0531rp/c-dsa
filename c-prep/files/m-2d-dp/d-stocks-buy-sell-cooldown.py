"""
309. Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(idx, buying):
            if idx >= len(prices):
                return 0
            if (idx, buying) in dp:
                return dp[(idx, buying)]
            
            cooldown = dfs(idx + 1, buying)
            if buying:
                buy = dfs(idx + 1, False) - prices[idx]
                dp[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx + 2, True) + prices[idx]
                dp[(idx, buying)] = max(sell, cooldown)
            return dp[(idx, buying)]
        return dfs(0, True)