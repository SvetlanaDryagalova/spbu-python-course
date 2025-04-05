def matrix_size(a: list[list[float]]):
    """
    Calculate the size of matrix and check if tro rows are not the same length.
    """
    rows = len(a)
    col = len(a[0])
    for i in range(1, len(a)):
        if len(a[i]) != col:
            raise ValueError("The rows of the matrix must be of the same length!")
    return [rows, cols]
def matrix_sum(
    a: list[list[float]] = None, b: list[list[float]] = None
) -> list[list[float]]:
    """
    Calculate the sum of two matrices.

    Parameters

     a: list[list[float]]  (the first input matrix)

     b: list[list[float]]  (the second input matrix)

    Returns

     c: list[list[float]]  (the matrix of sum of the input matrices)

    Raises

     TypeError

        If elements of the matrices are of the inappropriate type.

     ValueError

        If the row lengths in the matrix are not equal.

        If the size of one of the matrices is 0.

        If the sizes of the matrices are not equal.
    """
    if any(not isinstance(el, float) for el in a) or any(
        not isinstance(el, float) for el in b
    ):
        raise TypeError("Elements of the matrices must be float")

    sizes = matrix_size(a)
    if sizes != matrix_size(b):
        raise ValueError("Matrices must be of same dimensions!")
    if any(a is None, b is None):
        raise ValueError("Matrices must not be empty!")
    c = [[0] * sizes[0]] * sizes[1]
    for i in range(sizes[0]):
        for j in range(sizes[1]):
            c[i][j] = a[i][j] + b[i][j]
    return c

def matrix_multiply(
    a: list[list[float]] = None, b: list[list[float]] = None
) -> list[list[float]]:
    """
    Calculate the multiplication of two matrices.

    Parameters

     a: list[list[float]]  (the first input matrix)

     b: list[list[float]]  (the second input matrix)

    Returns

    c: list[list[float]]  (the matrix of multiplication of the input matrices)

    Raises

     TypeError

        If elements of the matrices are of the inappropriate type.

     ValueError

        If the row lengths in the matrix are not equal.

        If the sizes of one of the matrices don't make it possible to multiply.

        If the sizes of the matrices are 0.
    """
    if any(not isinstance(el, float) for el in a) or any(
        not isinstance(el, float) for el in b
    ):
        raise TypeError("Elements of the matrices must be float")

    a_size = matrix_size(a)
    b_size = matrix_size(b)
    if a_size[0] != b_size[1] or a_size[1] != b_size[0]:
        raise ValueError("Matrices cannot be multiplied because of the wrong sizes!")
    if any(a is None, b is None):
        raise ValueError("Matrices must not be empty!")
    c = [[0] * a_size[0]] * b_size[1]
    for i in range(a_size[0]):
        c[i][j] = sum([a[i][j] * b[j][i] for j in range(a_size[1])])
    return c

def matrix_transpose(a: list[list[float]] = None) -> list[list[float]]:
    """

    Calculate the multiplication of two matrices.

    Parameters

     a: list[list[float]]  (the input matrix)

    Returns

     ta: list[list[float]]  (the transposed matrix)

    Raises

     TypeError

        If elements of the matrix are of the inappropriate type.

     ValueError

        If the row lengths in the matrix are not equal.

        If the size of the matrix is 0.
    """
    if any(not isinstance(el, float) for el in a):
        raise TypeError("Elements of the matrix must be float!")
    if any(a is None):
        raise ValueError("Matrix must not be empty!")
    a_size = matrix_size(a)
    ta = [[0] * a_size[1]] * a_size[0]
    for i in range(a_size[0]):
        for j in range(a_size[1]):
            ta[j][i] = a[i][j]
    return ta
