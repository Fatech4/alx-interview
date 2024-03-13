#!/usr/bin/python3
""" A program that does the prime game """


def isWinner(x, nums):
    """ The function that checks the winner """
    def sieve_of_eratosthenes(n):
        """ The function that sieve the winners """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n + 1) if primes[i]]

    def calculate_winner(n):
        """ The function that calculates the winner """
        primes = sieve_of_eratosthenes(n)
        num_primes = len(primes)
        if num_primes % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = [calculate_winner(n) for n in nums]
    ben_wins = winners.count("Ben")
    maria_wins = winners.count("Maria")

    if ben_wins == maria_wins:
        return None
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return "Maria"
