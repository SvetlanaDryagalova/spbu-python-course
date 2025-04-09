from math import sqrt, acos, degrees
from typing import List


def dot_product(v: List[float], u: List[float]):
    """
    Calculate the dot product of two vectors.

    Parameters

     v: List[float]  (the first input vector)

     u: List[float]  (the second input vector)

    Returns

     float  (the dot product of the vectors)

    Raises

     TypeError

        If coordinates of the vector are of the inappropiate type.

     ValueError

        If the length of one of the vectors is 0.

        If the lengths of the vectors are not equal.
    """
    if any(not isinstance(el, float) for el in v) or any(
        not isinstance(el, float) for el in u
    ):
        raise TypeError("Coordinates of the vector must be float!")
    if v is None or u is None:
        raise ValueError("Vector must not be empty!")
    if len(v) != len(u):
        raise ValueError("Vectors must have the same length!")
    return sum(v[i] * u[i] for i in range(len(v)))


def vector_length(v: List[float]):
    """
    Calculate the length of a vector.

    Parameters

     v: List[float]  (the input vector)

    Raises

     ValueError

        If the length of one of the vectors is 0.

    Returns

     float (the length of the vector)
    """
    if not v:
        raise ValueError("Vector must not be empty!")
    return sqrt(sum(v[i] ** 2 for i in range(len(v))))


def angle_vectors(v: List[float], u: List[float]):
    """
    Calculate the angle between two vectors in degrees.

    Parameters

     v: List[float]  (the first input vector)

     u: List[float]  (the second input vector)

    Returns

     float  (the angle between two vectors in degrees)

    Raises

     TypeError

        If coordinates of the vector are of the inappropriate type.

     ValueError

        If the length of one of the vectors is 0.

        If the lengths of the vectors are not equal.
    """
    if any(not isinstance(el, float) for el in v) or any(
        not isinstance(el, float) for el in u
    ):
        raise TypeError("Coordinates of the vector must be float!")
    if v is None or u is None:
        raise ValueError("Vector must not be empty!")
    if len(v) != len(u):
        raise ValueError("Vectors must have the same length!")
    return degrees(acos(dot_product(v, u) / (vector_length(v) * vector_length(u))))
