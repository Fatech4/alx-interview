#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total """


def makeChange(coins, total):
    """ Initialize an array to store the minimum number of coins needed
    for each amount """
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total of 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp[i] for all i using the current coin
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    """ If dp[total] is still infinity, it means total cannot be met by
    any number of coins """
    if dp[total] == float('inf'):
        return -1

    # Return the minimum number of coins needed for the total amount
    return dp[total]
