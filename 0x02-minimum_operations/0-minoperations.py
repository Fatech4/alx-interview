#!/usr/bin/python3
''' In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given a
number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file. '''


def minOperations(n):
    if n == 1:
        return 0  # Already have 1 H, no operations needed

    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 0 operations needed for 1 H

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
