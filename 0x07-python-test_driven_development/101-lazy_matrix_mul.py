#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a function that multiplies 2 matrices by using the module NumPy
"""
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """Returns product of two matrices

    Args:
        m_a(matrix of int/float):first matrix
        m_b(matrix of int/float):second matrix
    """

    return(npy.matmul(m_a, m_b))
