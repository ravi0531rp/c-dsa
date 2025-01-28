"""
322. Coin Change

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""
import math
from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        idx = 1
        while idx <= amount:
            for coin in coins:
                if coin <= idx:
                    dp[idx] = min(dp[idx], 1 + dp[idx - coin])
            idx += 1
        return -1 if math.isinf(dp[-1]) else dp[-1]
        