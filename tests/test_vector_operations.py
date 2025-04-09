# Test module for vector operations
import pytest
from project.vector_operations import *

"""Valid tests"""


# test for dot_product
def test_dot_product_valid():
    v = [1.0, 2.0]
    u = [3.0, 4.0]
    expected_result = 11.0
    result = dot_product(v, u)
    assert result == expected_result


# test for vector_length
def test_vector_length_valid():
    v = [3.0, 4.0]
    expected_result = 5
    result = vector_length(v)
    assert round(result, 2) == expected_result


# test for angle_vectors
def test_angle_vectors_valid():
    v = [1.0, 0.0]

    u = [0.0, 1.0]
    expected_result = 90.0
    result = angle_vectors(v, u)
    assert round(result, 2) == expected_result


"""Tests with invalid type"""


# test for dot_product
def test_dot_product_invalid_type():
    v = ["a", "b"]

    u = ["c", "d"]
    with pytest.raises(TypeError):
        dot_product(v, u)


# test for vector_length
def test_vector_length_invalid_type():
    v = ["a", "b"]
    with pytest.raises(TypeError):
        vector_length(v)


# test for angle_vectors
def test_angle_vectors_invalid_type():
    v = ["a", "b"]

    u = ["c", "d"]
    with pytest.raises(TypeError):
        angle_vectors(v, u)


"""Tests with empty vector"""


# test for dot_product
def test_dot_product_empty_vector():
    v = []

    u = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError):
        dot_product(v, u)


# test for vector_length
def test_vector_length_empty_vector():
    v = []
    with pytest.raises(ValueError):
        vector_length(v)


# test for angle_vectors
def test_angle_vectors_empty_vector():
    v = []

    u = []
    with pytest.raises(ValueError):
        angle_vectors(v, u)


"""Tests with  unequal length"""


# test for dot_product
def test_dot_product_unequal_length():
    v = [1.0, 2.0]

    u = [3.0, 4.0, 5.0]
    with pytest.raises(ValueError):
        dot_product(v, u)


# test for angle_vectors
def test_angle_vectors_unequal_length():
    v = [1.0, 2.0]

    u = [3.0, 4.0, 5.0]
    with pytest.raises(ValueError):
        angle_vectors(v, u)
