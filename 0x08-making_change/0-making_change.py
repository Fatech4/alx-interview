#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total """


def makeChange(coins, total):
    if total <= 0:
        return 0
    """ Initialize a list to store the minimum number of coins
    needed for each total amount """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0
    # Iterate through all possible total amounts up to the given total
    for i in range(1, total + 1):
        """ For each total amount, iterate through all available coin
        denominations """
        for coin in coins:
            """ If the current coin denomination is less than or equal
            to the current total amount,
            # check if using this coin plus the minimum number of
            coins needed for the remaining amount
            # results in a smaller number of coins than what we
            have previously calculated. """
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    """ If the value of dp[total] remains float('inf'), it means
    it's not possible to make the total amount with the given coins """
    if dp[total] == float('inf'):
        return -1

    return dp[total]
