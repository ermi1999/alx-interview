#!/usr/bin/python3
"""
module for lockboxes
"""
from sys import setrecursionlimit


def openRecursively(originalBox, openedBox, openedBoxes):
    """
    Recursive function to solve the boxes
    """
    setrecursionlimit(2000)
    notOpened = set(openedBox) - openedBoxes
    for key in notOpened:
        if key < len(originalBox):
            openedBoxes.add(key)
            openRecursively(originalBox, originalBox[key], openedBoxes)


def canUnlockAll(boxes):
    """
    Method to determine if all boxes can be opened
    """
    if len(boxes) < 2:
        return True
    openedBoxes = set([0])
    for key in boxes[0]:
        if key not in openedBoxes:
            if key < len(boxes):
                openedBoxes.add(key)
                openRecursively(boxes, boxes[key], openedBoxes)
    if len(openedBoxes) == len(boxes):
        return True
    return False
