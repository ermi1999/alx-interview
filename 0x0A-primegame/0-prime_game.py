#!/usr/bin/python3
"""Prime game"""
from typing import List


def findPrime(n: int) -> List[int]:
    """finds all prime numbers for n"""
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    result = []
    for p in range(2, n + 1):
        if prime[p]:
            result.append(p)
    return result

def isWinner(x, nums):
    """Prime game"""
    primeCache = {}
    maria = 0
    ben = 0
    for i in range(x):
        if nums[i] in primeCache:
            primes = primeCache[nums[i]]
        else:
            primes = findPrime(nums[i])
            primeCache[nums[i]] = primes
        if not primes:
            ben += 1
            continue
        removedNums = []
        j = 0
        turn = "maria"
        while j < len(primes):
            prime = primes[j]
            if prime in removedNums:
                while ((prime not in removedNums) and (j < len(primes))):
                    prime = primes[j]
                    j += 1
                if prime in removedNums:
                    if turn == "maria":
                        maria += 1
                    else:
                        ben += 1
                    break
            for k in range(prime, nums[i] + 1, prime):
                removedNums.append(k)
            if turn == "maria":
                turn = "ben"
            else:
                turn = "maria"
            j += 1
            if j >= len(primes):
                if turn == "maria":
                    ben += 1
                else:
                    maria += 1
    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
        
        