from typing import List


def matrix_size(a: List[List[float]]):
    """
    Calculate the size of matrix and check if tro rows are not the same length.
    """
    if not a:
        raise ValueError("Matrix must not be empty!")
    rows = len(a)
    cols = len(a[0])
    for row in a:
        if len(row) != cols:
            raise ValueError("The rows of the matrix must be of the same length!")
    return [rows, cols]


def matrix_sum(a: List[List[float]], b: List[List[float]]):
    """
    Calculate the sum of two matrices.

    Parameters

     a: List[List[float]]  (the first input matrix)

     b: List[List[float]]  (the second input matrix)

    Returns

     c: List[List[float]]  (the matrix of sum of the input matrices)

    Raises

     TypeError

        If elements of the matrices are of the inappropriate type.

     ValueError

        If the row lengths in the matrix are not equal.

        If the size of one of the matrices is 0.

        If the sizes of the matrices are not equal.
    """
    if any(not isinstance(el, float) for row in a for el in row) or any(
        not isinstance(el, float) for row in b for el in row
    ):
        raise TypeError("Elements of the matrices must be float")

    sizes = matrix_size(a)
    if sizes != matrix_size(b):
        raise ValueError("Matrices must be of same dimensions!")
    if not a or not b:
        raise ValueError("Matrices must not be empty!")
    c = [[0.0 for _ in range(sizes[1])] for _ in range(sizes[0])]
    for i in range(sizes[0]):
        for j in range(sizes[1]):
            c[i][j] = float(a[i][j]) + float(b[i][j])
    return c


def matrix_multiply(a: List[List[float]], b: List[List[float]]):
    """
    Calculate the multiplication of two matrices.

    Parameters

     a: List[List[float]]  (the first input matrix)

     b: List[List[float]]  (the second input matrix)

    Returns

    c: List[List[float]]  (the matrix of multiplication of the input matrices)

    Raises

     TypeError

        If elements of the matrices are of the inappropriate type.

     ValueError

        If the row lengths in the matrix are not equal.

        If the sizes of one of the matrices don't make it possible to multiply.

        If the sizes of the matrices are 0.
    """
    if any(not isinstance(el, float) for row in a for el in row) or any(
        not isinstance(el, float) for row in b for el in row
    ):
        raise TypeError("Elements of the matrices must be float")

    a_size = matrix_size(a)
    b_size = matrix_size(b)
    if a_size[1] != b_size[0]:
        raise ValueError("Matrices cannot be multiplied because of the wrong sizes!")
    if not a or not b:
        raise ValueError("Matrices must not be empty!")
    c = [[0.0 for _ in range(b_size[1])] for _ in range(a_size[0])]
    for i in range(a_size[0]):
        for j in range(b_size[1]):
            for k in range(a_size[1]):
                c[i][j] += a[i][k] * b[k][j]
    return c


def matrix_transpose(a: List[List[float]]):
    """

    Calculate the multiplication of two matrices.

    Parameters

     a: List[List[float]]  (the input matrix)

    Returns

     ta: List[List[float]]  (the transposed matrix)

    Raises

     TypeError

        If elements of the matrix are of the inappropriate type.

     ValueError

        If the row lengths in the matrix are not equal.

        If the size of the matrix is 0.
    """
    if any(not isinstance(el, float) for row in a for el in row):
        raise TypeError("Elements of the matrix must be float!")
    if not a:
        raise ValueError("Matrix must not be empty!")
    a_size = matrix_size(a)
    ta = [[0.0 for _ in range(a_size[0])] for _ in range(a_size[1])]
    for i in range(a_size[0]):
        for j in range(a_size[1]):
            ta[j][i] = a[i][j]
    return ta
