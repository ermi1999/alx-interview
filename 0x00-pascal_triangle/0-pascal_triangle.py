#!/usr/bin/python3
"""
Module for pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    arr = []
    for i in range(n):
        arr_i = []
        arr_i.append(1)
        if i == 1:
            arr_i.append(1)
            arr.append(arr_i)
            continue
        if i == 0:
            arr.append(arr_i)
            continue
        for j in range(1, i):
            arr_i.append(arr[i - 1][j - 1] + arr[i - 1][j])
        arr_i.append(1)
        arr.append(arr_i)
    return arr
