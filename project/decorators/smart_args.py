from functools import wraps
import inspect


class Evaluated:
    """
    Wrapper class that ensures the function passed is evaluated
    when called. Raises a TypeError if an Isolated class is passed to it.
    """

    def __init__(self, func_without_args) -> None:
        """
        Initialize with a function. Raises an error if the function
        is an instance of the Isolated class.
        Parameters
            func_without_args: A callable to be wrapped.
        Raises
            TypeError
            If the first argument is not a callable object.
        """
        if not callable(func_without_args):
            raise TypeError("First argument must be a callable object.")
        self.func = func_without_args


class Isolated:
    """
    A marker class indicating that the argument should be copied.
    """

    pass


def smart_args(func):
    """
    A decorator that handles the arguments passed to a function, with special
    regard to Isolated and Evaluated instances.
    Arguments marked as Isolated are deep copied.
    Arguments marked Evaluated result in a call to the wrapped function.
    Parameters
        func : The function to be wrapped.
    Raises
        ValueError
            If an argument uses the 'Isolated' without value.
            If an argument marked as Isolated is not provided.
    Returns
        The wrapped function with smart argument processing.
    """

    sig = inspect.signature(func)
    new_params = {}

    @wraps(func)
    def wrapper(**kwargs):
        nonlocal new_params

        for name, param in sig.parameters.items():
            if param.default is param.empty:
                new_params[name] = kwargs.get(name)
                continue

            if name in kwargs:
                new_params[name] = kwargs[name]
            else:
                default_value = param.default

                if isinstance(default_value, Evaluated):
                    new_params[name] = default_value.func()
                elif isinstance(default_value, Isolated):
                    raise ValueError(
                        f"Argument '{name}' must not use 'Isolated' without value."
                    )
                else:
                    new_params[name] = default_value

        for name, value in kwargs.items():
            if isinstance(value, Evaluated) or isinstance(value, Isolated):
                raise ValueError(
                    f"Argument '{name}' can't be mixed with Evaluated or Isolated."
                )

        return func(**new_params)

    return wrapper
