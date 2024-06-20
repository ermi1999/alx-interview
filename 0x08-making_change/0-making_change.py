#!/usr/bin/python3
"""module for finding the minimum number of
coins needed to make a change"""


def makeChange(coins, total):
    """function for finding the minimum number of
    coins needed to make a change"""
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1