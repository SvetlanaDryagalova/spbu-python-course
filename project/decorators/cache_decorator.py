from collections import OrderedDict
from functools import wraps


def cache(max_cache_size: int = 0):
    """
    Decorator for caching the results of a function with optional support for keyword arguments
    and a size limit on the cache.
    Parameters
        max_cache_size (int) : The maximum size of the cache.

    Returns
        function : The decorated function with caching applied.

    Raises
        ValueError
            If `max_cache_size` is not an integer.
            If `max_cache_size` is a negative integer.
    """
    if not isinstance(max_cache_size, int):
        raise ValueError(f"`max_cache_size` must be an integer, got {type(max_cache_size).__name__}")
    
    if max_cache_size < 0:
        raise ValueError("The parameter must be a non-negative integer")

    cached = {}

    def decorator(func):
        func.cache = {}
        func.cache_size = max_cache_size
        
        def wrapper(*args):
            if args in func.cache:
                return func.cache[args]
            result = func(*args)
            func.cache[args] = result
            
            if len(func.cache) > max_cache_size:
                # Удаляем старый элемент (первый добавленный)
                func.cache.pop(next(iter(func.cache)))
            return result
        
        return wrapper
    
    return decorator
