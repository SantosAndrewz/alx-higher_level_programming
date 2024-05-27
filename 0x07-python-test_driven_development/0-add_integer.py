#!/usr/bin/python3
"""
Module for addition of two integers.
"""


def add_integer(a, b=98):
    """
    Function adds two integers.

    Args:
        a (int or float): first digit.
        b (int or float): second digit. Default=98.

    Returns:
        int: Sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
