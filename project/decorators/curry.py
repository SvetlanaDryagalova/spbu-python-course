def curry_explicit(function, arity: int):
    """
    Partial application (currying) of a function with a specified arity.
    Parameters
        function : The function to be curried.
        arity (int) : The required arity of the function after currying.
    Returns
        A curried function
    Raises
        TypeError
            If the first argument is not a callable object.
        ValueError
            If the arity is a negative integer.
    """
    if not callable(function):
        raise TypeError("First argument must be a callable object.")

    if arity == 0:
        return function
    if arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    def _curried(*args):
        if len(args) > arity:
            return function(*args[:arity])
        elif len(args) < arity:

            def partial():
                return _curried(*args, *function(*args))

            return partial
        else:
            return function(*args)

    return _curried


def uncurry_explicit(function, arity: int):
    """
    Partial application (currying) of a function with a specified arity.
    Parameters
        function : The function to be curried.
        arity (int) : The required arity of the function after currying.
    Returns
        A curried function
    Raises
        TypeError
            If the first argument is not a callable object.
        ValueError
            If the arity is a negative integer.
            If the numbers of arguments are not equal.

    """
    if not callable(function):
        raise TypeError("First argument must be a callable object.")

    def _uncurried(*args):
        if len(args) != arity:
            raise ValueError(f"Expected {arity} arguments")
        if len(args) >= arity:
            args = list(args)
            return function(*args)
        else:
            return lambda *rest: _uncurried(*args, *rest)

    return _uncurried
