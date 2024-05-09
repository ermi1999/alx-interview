#!/usr/bin/python3
"""
module for finding the number of operations
that will took to paste in n number of hashes.
"""
import math


def minOperations(n):
    """
    this function tries to find
    the minimum operations that will
    took to paste n number of hashes using factorials.
    """
    factors = []
    while n % 2 == 0:
        factors.append(2),
        n = n // 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i),
            n = n // i
    if n > 2:
        factors.append(n)

    return sum(factors)
