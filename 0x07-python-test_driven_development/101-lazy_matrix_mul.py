#!/usr/bin/python3

"""Contains a function that multiplies two matrices"""

import numpy as numpy

def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of two matrices

    Args:
        m_a : matrix 1
        m_b : matrix 2
    """

    return (np.matmul(m_a, m_b))