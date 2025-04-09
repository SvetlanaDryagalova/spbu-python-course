import pytest
from project.decorators.curry import curry_explicit, uncurry_explicit


def test_curry_explicit_no_arguments():
    """Tests that currying works without any initial arguments."""

    def add(x, y):
        return x + y

    curried_add = curry_explicit(add, 2)
    assert curried_add(1, 2) == 3
    assert curried_add(1)(2) == 3


def test_curry_explicit_with_extra_arguments():
    """Tests that extra arguments are ignored by the curried function."""

    def add(x, y):
        return x + y

    curried_add = curry_explicit(add, 2)
    assert curried_add(1, 2, 3) == 3  # ignores extra argument


def test_curry_explicit_zero_arity():
    """Tests that zero arity functions can be curried."""

    def greet():
        return "Hello"

    curried_greet = curry_explicit(greet, 0)
    assert curried_greet() == "Hello"


def test_curry_explicit_negative_arity():
    """Tests that negative arities raise a ValueError."""
    with pytest.raises(ValueError, match="Arity must be a non-negative integer"):
        curry_explicit(lambda x: x, -1)


def test_curry_explicit_not_callable():
    """Tests that non-callables raise a TypeError."""
    with pytest.raises(TypeError, match="First argument must be a callable object."):
        curry_explicit(123, 2)


def test_uncurry_explicit():
    """Tests that uncurrying works correctly."""

    def add(x, y):
        return x + y

    uncurried_add = uncurry_explicit(add, 2)
    assert uncurried_add(1, 2) == 3


def test_uncurry_explicit_wrong_number_arguments():
    """Tests that incorrect number of arguments raises a ValueError."""
    uncurried_add = uncurry_explicit(lambda x, y: x + y, 2)
    with pytest.raises(ValueError, match="Expected 2 arguments"):
        uncurried_add(1)


def test_uncurry_explicit_not_callable():
    """Tests that non-callables raise a TypeError."""
    with pytest.raises(TypeError, match="First argument must be a callable object."):
        uncurry_explicit(123, 2)


def test_uncurry_explicit_with_varargs():
    """Tests that varargs work correctly with uncurrying."""

    def concat(*args):
        return "".join(args)

    uncurried_concat = uncurry_explicit(concat, 3)
    assert uncurried_concat("Hello", " ", "World") == "Hello World"
