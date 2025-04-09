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
    
    # Проверка на неотрицательность
    if max_cache_size < 0:
        raise ValueError("The parameter must be a non-negative integer")

    cached = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Формируем ключ для кэша
            kwargs_key = frozenset(kwargs.items())
            key = (args, kwargs_key)
            
            # Проверяем наличие ключа в кэше
            if key in cached:
                return cached[key]
            
            # Вычисляем результат и сохраняем его в кэш
            result = func(*args, **kwargs)
            cached[key] = result
            return result
        
        return wrapper
    
    return decorator
