#!/usr/bin/python3
"""
Module for text_indentation function
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    
    Args:
        text: The text to be printed (must be a string).
    
    Raises:
        TypeError: If text is not a string.
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    skip_space = False
    
    for char in text:
        if char in ".?:":
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False
    
    print(result.strip(), end="")

