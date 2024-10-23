#!/usr/bin/python3
"""
Module for say_my_name function
"""

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".
    
    Args:
        first_name: The first name (string).
        last_name: The last name (string), optional.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")

