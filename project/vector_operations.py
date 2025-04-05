from math import sqrt, acos

def dot_product(v : list[int, float]=None, u : list[int, float]=None):
    """
       Calculate the dot product of two vectors.
       Parameters
        v : list[int, float]  (the first input vector)
        u : list[int, float]  (the second input vector)
       Returns
        float, int  (the dot product of the vectors)
       Raises
        ValueError
            If the length of one of the vectors is 0.
            If the lengths of the vectors are not equal.
    """
    if any(not isinstance(el, int) or not isinstance(el, float) for el in v) \
            or any(not isinstance(el, int) or not isinstance(el, float) for el in u):
        raise TypeError('Coordinates of the vector must be digits!')
    if any(v is None or u is None):
        raise ValueError('Vector must not be empty!')
    if len(v)!=len(u):
        raise ValueError('Vectors must have the same length!')
    return sum(v[i] * u[i] for i in range(len(v)))

def vector_length(v : list[int, float]=None):
    """
        Calculate the length of a vector.
        Parameters
         v : list[int, float]  (the input vector)
        Returns
         float, int (he length of the vector)
    """
    return sqrt(sum(v[i]**2 for i in range(len(v))))

def angle_vectors(v : list[int, float]=None, u : list[int, float]=None):
    """
       Calculate the angle between two vectors in degrees.
       Parameters
        v : list[int, float]  (the first input vector)
        u : list[int, float]  (the second input vector)
       Returns
        float  (the angle between two vectors in degrees)
       Raises
        TypeError
            If coordinates of the vector are of the wrong type.
        ValueError
            If the length of one of the vectors is 0.
            If the lengths of the vectors are not equal.
    """
    return degrees(acos(dot_product(v, u) / (vector_length(v) * vector_length(u))))

