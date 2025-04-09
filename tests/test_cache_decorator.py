import pytest
from project.decorators.cache_decorator import cache
from datetime import datetime


@pytest.mark.parametrize("max_cache_size", [-1, "abc", 0.5])
def test_cache_decorator_with_invalid_arguments(max_cache_size):
    """Tests that invalid values for `max_cache_size` raises an exception."""
    
    with pytest.raises(ValueError):
        @cache(max_cache_size)
        def dummy_function():
            pass


def test_cache_works_for_positive_values():
    """Tests that caching works properly for positive values of `max_cache_size`."""

    @cache(1)
    def square(n):
        return n**2

    # Check that the cache stores correct results
    assert square(2) == 4
    assert square(2) == 4

    # Make sure max cache size limits work
    square(3)
    square(4)
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

    # Check that older items get removed from the cache
    square(5)
    assert len(square.cache) == 1
    assert square(4) == 16


def test_keyword_arguments_are_considered_in_the_cache():
    """Tests that keyword arguments are considered in the cache key."""

    @cache(2)
    def add_one(a, b=1):
        return a + b

    # Arguments without keywords should use the same key
    assert add_one(1) == 2
    assert add_one(1) == 2

    # Different keywords should create different keys
    assert add_one(1, b=2) == 3
    assert add_one(1, b=2) == 3
    assert add_one(1, b=3) == 4

    # Multiple different combinations should store separate results
    assert add_one(2, b=1) == 3
    assert add_one(2, b=2) == 4
    assert add_one(2, b=3) == 5

    # Clean up the cache
    del add_one.cache


def test_function_is_properly_wrapped():
    """Tests that the wrapped function maintains its original attributes."""

    @cache(2)
    def my_func():
        return 1

    assert my_func.__name__ == "my_func"
    assert my_func.__doc__ == ""


def test_cache_clears_on_new_day():
    """Tests that the cache clears itself every day at midnight."""

    @cache(1)
    def increment(num):
        return num + 1

    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = now + datetime.timedelta(days=1)

    increment(1)
    assert increment.cache["(1, frozenset({}))"] == 2

    datetime.sleep((tomorrow - now).total_seconds())

    assert increment.cache == {}

    increment(1)
    assert increment.cache["(1, frozenset({}))"] == 2
