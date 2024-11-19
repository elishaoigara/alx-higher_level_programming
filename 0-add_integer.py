#!/usr/bin/python3
"""
Module for add_integer function
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to integers).
    
    Args:
        a: first number, must be int or float.
        b: second number, default is 98, must be int or float.

    Returns:
        The sum of the two integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

