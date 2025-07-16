#!/usr/bin/python3
"""
Pascal's Triangle module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): Number of rows in Pascal's triangle

    Returns:
        list: List of lists representing Pascal's triangle
              Empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            for j in range(1, i):
                value = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(value)

            row.append(1)

        triangle.append(row)

    return triangle
