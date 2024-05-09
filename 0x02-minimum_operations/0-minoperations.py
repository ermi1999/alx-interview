#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n: int) -> int:
    """
    minimum operations
    """
    clipboard = 1
    h = 1
    numberOfOperations = 0

    while h < n:
        if n % h == 0:
            clipboard = h
            h += clipboard
            numberOfOperations += 2
        else:
            h += clipboard
            numberOfOperations += 1

    if h != n:
        return 0
    return numberOfOperations
