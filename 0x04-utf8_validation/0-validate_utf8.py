#!/usr/bin/python3
"""
UTF-8 Validation.
"""


def validUTF8(data):
    """
    UTF-8 Validation.
    """
    for num in data:
        if num > 255:
            return False
    return True