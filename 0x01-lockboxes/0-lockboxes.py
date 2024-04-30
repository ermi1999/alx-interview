#!/usr/bin/python3
"""
module for lockboxes
"""


def solveRecursively(originalBox, openedBox, openedBoxes):
    """
    Recursive function to solve the boxes
    """
    notOpened = set(openedBox) - openedBoxes
    for key in notOpened:
        openedBoxes.add(key)
        solveRecursively(originalBox, originalBox[key], openedBoxes)


def canUnlockAll(boxes):
    """
    Method to determine if all boxes can be opened
    """
    openedBoxes = set([0])
    for key in boxes[0]:
        if key not in openedBoxes:
            openedBoxes.add(key)
            solveRecursively(boxes, boxes[key], openedBoxes)
    if len(openedBoxes) == len(boxes):
        return True
    return False
