from collections import OrderedDict
from functools import wraps


def cache(max_cache_size: int = 0):
    """
    Decorator for caching the results of a function with optional support for keyword arguments
    and a size limit on the cache.
    Parameters
        max_cache_size (int) : The maximum size of the cache.

    Returns
        function: The decorated function with caching applied.

    Raises:
        ValueError
            If `max_cache_size` is a negative integer.
    """
    if max_cache_size < 0:
        raise ValueError("The parameter must be a non-negative integer")

    def _cache(func):
        cached = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs_key = frozenset(kwargs.items())
            key = (args, kwargs_key)

            if key in cached:
                return cache[key]

            result = func(*args, **kwargs)

            cached[key] = result

            if max_cache_size > 0 and len(cached) > max_cache_size:
                cached.popitem(last=False)

            return result

        return wrapper

    return _cache
