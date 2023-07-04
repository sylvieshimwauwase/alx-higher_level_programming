#!/usr/bin/python3
"""Multiplying 2 matrices using Numpy module"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplying 2 matrices using Numpy module

    Args:
        m_a (list): matrix A represented as list of integer
        m_b (list): matrix B represented as list of integer

    Returns:
        list: Result of multiplication of two matrixes

    Raises:
        ValueError: If m_a and m_b can't  be multiplied
    """

    res = np.matmul(m_a, m_b)
    return res
