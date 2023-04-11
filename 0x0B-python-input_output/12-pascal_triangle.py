#!/usr/bin/python3
"""This Module defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Function Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tris = triangles[-1]
        tmp = [1]
        for i in range(len(tris) - 1):
            tmp.append(tris[i] + tris[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
