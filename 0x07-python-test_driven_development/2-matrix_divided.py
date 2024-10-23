#!/usr/bin/python3
"""
Module for matrix_divided function
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    
    Args:
        matrix: A list of lists of integers/floats.
        div: A number (integer or float) which will divide the matrix elements.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
                   If each row of the matrix is not the same size.
                   If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(num / div, 2) for num in row] for row in matrix]

