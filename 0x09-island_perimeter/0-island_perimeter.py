#!/usr/bin/python3
"""
module for finding an island peimeter.
"""


def island_perimeter(grid):
    """Function for finding an island perimeter."""
    perimeter = 0
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            if grid[col][row]:
                temp = 4
                if col - 1 >= 0:
                    if grid[col - 1][row]:
                        temp -= 1
                if col + 1 < len(grid):
                    if grid[col + 1][row]:
                        temp -= 1
                if row + 1 < len(grid[col]):
                    if grid[col][row + 1]:
                        temp -= 1
                if row - 1 >= 0:
                    if grid[col][row - 1]:
                        temp -= 1
                perimeter += temp
    return perimeter
