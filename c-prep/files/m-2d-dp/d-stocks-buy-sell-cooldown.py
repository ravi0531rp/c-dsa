"""
309. Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


"""
class Solution:
    def maxProfit(self, stocks):
        dp = {}
        BUYING = 1
        SELLING = 0

        def dfs(index, state):
            if index == len(stocks):
                return 0
            if (index, state) in dp:
                return dp[(index,state)]

            if state == BUYING:
                buying_profit = dfs(index+1, SELLING) - stocks[index]
                cooldown_profit = dfs(index+1, BUYING)
                dp[(index, state)] = max(buying_profit, cooldown_profit)
            else:
                selling_profit = dfs(index+2, BUYING) + stocks[index]
                cooldown_profit = dfs(index+1, BUYING) 
                dp[(index, state)] = max(selling_profit, cooldown_profit)
            return dp[(index, state)]
        return dfs(0, BUYING)

        
