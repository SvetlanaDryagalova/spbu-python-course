# Test module for matrix operations
import pytest
from project.matrix_operations import *

"""Valid tests"""
# tests for matrix_sum
def test_matrix_sum_valid1():
    m1 = [[4.0, 1.0], [8.0, 2.0]]
    m2 = [[3.0, 9.0], [2.0, 4.0]]
    expected_result = [[7.0, 10.0], [10.0, 5.0]]
    result = matrix_sum(m1, m2)
    assert result == expected_result
def test_matrix_sum_valid2():
    m1 = [[-1.0, 3.0], [0.0, 1.0], [-2.0, 2.0]]
    m2 = [[2.0, 0.0], [-1.0, 1.0], [3.0, -2.0]]
    expected_result = [[1.0, 3.0], [-1.0, 2.0], [1.0, 0.0]]
    result = matrix_sum(m1, m2)
    assert result == expected_result

# tests for matrix_multiply
def test_matrix_multiply_valid():
    m1 = [[3.0, -1.0, 2.0], [4.0, 2.0, 0.0], [-5.0, 6.0, 1.0]]
    m2 = [[8.0, 1.0], [7.0, 2.0], [2.0, -3.0]]
    expected_result = [[21.0, -5.0], [46.0, 8.0], [4.0, 4.0]]
    result = matrix_multiply(m1, m2)
    assert result == expected_result

# test for matrix_transpose
def test_matrix_transpose_valid():
    m = [[1.0, 50.0], [44.0, 34.0], [345.0, 0.0]]
    expected_result = [[1.0, 44.0, 345.0], [50.0, 34.0, 0.0]]
    result = matrix_transpose(m)
    assert result == expected_result

""" Tests with empty matrices"""
# test for matrix_sum
def test_matrix_sum_empty():
    empty_matrix = []

    m = [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]
    with pytest.raises(ValueError):
        matrix_sum(empty_matrix, m)

# test for matrix_multiply
def test_matrix_multiply_empty():
    empty_matrix = []

    m = [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 3.0, 3.0]]
    with pytest.raises(ValueError):
        matrix_multiply(empty_matrix, m)

# test for matrix_transpose
def test_matrix_transpose_empty():
    empty_matrix = []
    with pytest.raises(ValueError):
        matrix_transpose(empty_matrix)

"""Tests with unequal row length, row count and size"""
# tests for matrix_sum
def test_matrix_sum_unequal_length():
    m1 = [[1.0, 2.0, 3.0], [3.0, 4.0]]

    m2 = [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]
    with pytest.raises(ValueError):
        matrix_sum(m1, m2)
def test_matrix_sum_unequal_row_count():
    unequal_matrix = [[1.0, 2.0, 3.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]

    m2 = [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]
    with pytest.raises(ValueError):
        matrix_sum(unequal_matrix, m2)
def test_matrix_sum_unequal_size():
    m1 = [[1.0, 2.0, 3.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]

    m2 = [[1.0, 1.0], [2.0, 2.0]]
    with pytest.raises(ValueError):
        matrix_sum(m1, m2)

# tests for matrix_multiply
def test_matrix_multiply_unequal_length():
    unequal_matrix = [[1.0, 2.0, 3.0], [3.0, 4.0]]

    m2 = [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 3.0, 3.0]]
    with pytest.raises(ValueError):
        matrix_multiply(unequal_matrix, m2)
def test_matrix_multiply_unequal_size():
    m1 = [[1.0, 2.0, 3.0], [5.0, 6.0, 7.0]]

    m2 = [2.0, 2.0]
    with pytest.raises(ValueError):
        matrix_multiply(m1, m2)
# test for matrix_transpose
def test_matrix_transpose_unequal_length():
    unequal_matrix = [[1.0, 2.0, 3.0], [3.0, 4.0]]
    with pytest.raises(ValueError):
        matrix_transpose(unequal_matrix)

"""Tests with invalid type"""
# tests for matrix_sum
def test_matrix_sum_invalid_type():
    m1 = [[1.0, 2.0, 3.0], [1.0, "2.0", 3.0], [1.0, 2.0, 3.0]]

    m2 = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]
    with pytest.raises(TypeError):
        matrix_sum(m1, m2)
# tests for matrix_multiply
def test_matrix_multiply_invalid_type():
    m1 = [[1.0, 2.0, 3.0], [1.0, "2.0", 3.0], [1.0, 2.0, 3.0]]

    m2 = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]
    with pytest.raises(TypeError):
        matrix_multiply(m1, m2)
# tests for matrix_transpose
def test_matrix_transpose_invalid_type():
    m = [[1.0, 2.0, 3.0], [1.0, "2.0", 3.0], [1.0, 2.0, 3.0]]
    with pytest.raises(TypeError):
        matrix_transpose(m)
