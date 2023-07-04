#!/usr/bin/python3
"""Function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Multily two matrices

    Args:
        m_a (list): matrix A represented as list of integer
        m_b (list): matrix B represented as list of integer

    Returns:
        list: Result of multiplication of two matrixes

    Raises:
        TypeError: If m_a or m_b is not a list
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can'be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)

    return result
