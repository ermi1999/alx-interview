#!/usr/bin/python3
"""
minimum operations.
"""


def minOperations(n):
    """
    minimum operations.
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    h = 1
    numberOfOperations = 0
    clipboard = 0
    while h < n:
        if h + h < n:
            if clipboard > 0:
                if h + h > clipboard + h + 1:
                    print("copy and paste")
                    clipboard = h
                    h += clipboard
                    numberOfOperations += 2
                    continue
            else:
                print("copy and paste")
                clipboard = h
                h += clipboard
                numberOfOperations += 2
                continue
        print("paste")
        h += clipboard
        numberOfOperations += 1
    if h == n:
        return numberOfOperations
    return 0
