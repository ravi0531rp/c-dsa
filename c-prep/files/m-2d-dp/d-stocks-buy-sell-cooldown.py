"""
309. Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


"""

class Solution:

    def maxProfit(self, stocks):

        n = len(stocks)

        BUYING = 1
        SELLING = 0

        # n+2 because we access i+2
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):

            # BUYING state
            buying_profit = dp[i + 1][SELLING] - stocks[i]

            cooldown_profit = dp[i + 1][BUYING]

            dp[i][BUYING] = max(
                buying_profit,
                cooldown_profit
            )

            # SELLING state
            selling_profit = dp[i + 2][BUYING] + stocks[i]

            cooldown_profit = dp[i + 1][SELLING]

            dp[i][SELLING] = max(
                selling_profit,
                cooldown_profit
            )

        return dp[0][BUYING]

        
