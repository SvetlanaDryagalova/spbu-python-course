#Test module for matrix operations
import pytest
from matrix_operations import *

"""Valid tests"""
# tests for matrix_sum
def test_matrix_sum_valid1():
    m1 = [[4, 1], [8, 2]]
    m2 = [[3, 9], [2, 4]]
    expected_result = [[7, 10], [10, 5]]
    result = matrix_sum(m1, m2)
    assert result == expected_result
def test_matrix_sum_valid2():
    m1 = [[-1.0, 3.0], [0, 1], [-2, 2.0]]
    m2 = [[2, 0], [-1.0, 1], [3, -2.0]]
    expected_result = [[1, 3], [-1, 2], [1, 0]]
    result = matrix_sum(m1, m2)
    assert result == expected_result

# tests for matrix_multiply
def test_matrix_multiply_valid1():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    expected_result = [[9, 12], [21, 28]]
    result = matrix_multiply(m1, m2)
    assert result == expected_result
def test_matrix_multiply_valid2():
    m1 = [[3, -1.0, 2.0], [4, 2, 0.0], [-5, 6, 1]]
    m2 = [[8, 1.0], [7, 2], [2.0, -3.0]]
    expected_result = [[21.0, -5.0], [46.0, 8.0], [4.0, 4.0]]
    result = matrix_multiply(m1, m2)
    assert result == expected_result

# test for matrix_transpose
def test_matrix_transpose_valid():
    m = [[1, 50], [44, 34], [345, 0]]
    expected_result = [[1, 44, 345], [50, 34, 0]]
    result = matrix_transpose(m)
    assert result == expected_result

""" Tests with empty matrices"""
# test for matrix_sum
def test_matrix_sum_empty():
    empty_matrix = []
    m2 = [[1, 1, 1], [2, 2, 2]]
    with pytest.raises(ValueError):
        matrix_sum(empty_matrix, m2)

# test for matrix_multiply
def test_matrix_multiply_empty():
    empty_matrix = []
    m2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    with pytest.raises(ValueError):
        matrix_multiply(empty_matrix, m2)

# test for matrix_transpose
def test_matrix_transpose_empty():
    empty_matrix = []
    with pytest.raises(ValueError):
        matrix_transpose(empty_matrix)

"""Tests with unequal row length, row count and size"""
# tests for matrix_sum
def test_matrix_sum_unequal_length():
    m1 = [[1, 2, 3], [3, 4]]
    m2 = [[1, 1, 1], [2, 2, 2]]
    with pytest.raises(ValueError):
        matrix_sum(m1, m2)
def test_matrix_sum_unequal_row_count():
    unequal_matrix = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
    m2 = [[1, 1, 1], [2, 2, 2]]
    with pytest.raises(ValueError):
        matrix_sum(unequal_matrix, m2)
def test_matrix_sum_unequal_size():
    m1 = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
    m2 = [[1, 1], [2, 2]]
    with pytest.raises(ValueError):
        matrix_sum(m1, m2)

# tests for matrix_multiply
def test_matrix_multiply_unequal_length():
    unequal_matrix = [[1, 2, 3], [3, 4]]
    m2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    with pytest.raises(ValueError):
        matrix_multiply(unequal_matrix, m2)
def test_matrix_multiply_unequal_size():
    m1 = [[1, 2, 3], [5, 6, 7]]
    m2 = [2, 2]
    with pytest.raises(ValueError):
        matrix_multiply(m1, m2)
# test for matrix_transpose
def test_matrix_transpose_unequal_length():
    unequal_matrix = [[1, 2, 3], [3, 4]]
    with pytest.raises(ValueError):
        matrix_transpose(unequal_matrix)

"""Tests with invalid type"""
# tests for matrix_sum
def test_matrix_sum_invalid_type():
    m1 = [[1, 2.0, 3], [1, '2', 3], [1, 2, 3]]
    m2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    with pytest.raises(TypeError):
        matrix_sum(m1, m2)
# tests for matrix_multiply
def test_matrix_multiply_invalid_type():
    m1 = [[1, 2.0, 3], [1, '2', 3], [1, 2, 3]]
    m2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    with pytest.raises(TypeError):
        matrix_multiply(m1, m2)
# tests for matrix_transpose
def test_matrix_transpose_invalid_type():
    m = [[1, 2.0, 3], [1, '2', 3], [1, 2, 3]]
    with pytest.raises(TypeError):
        matrix_transpose(m)