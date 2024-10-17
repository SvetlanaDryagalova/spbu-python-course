from project.smart_args import smart_args, Evaluated, Isolated
import pytest


def test_evaluated_class_instantiation():
    """Test that the Evaluated class instantiates correctly."""

    def foo():
        pass

    e = Evaluated(foo)
    assert e.func == foo


def test_smart_args_wrapper_creation():
    """Test that the smart_args decorator creates a valid wrapper."""

    def bar(a, b=None, c='hello'):
        return a, b, c

    smart_bar = smart_args(bar)
    assert smart_bar.__name__ == 'bar'
    assert smart_bar.__module__ == '__main__'


def test_evaluated_usage_in_argument():
    """Test usage of Evaluated objects as function arguments."""

    def baz(a, b=Evaluated(lambda: 42)):
        return a, b

    smart_baz = smart_args(baz)
    assert smart_baz(1) == (1, 42)


def test_isolated_usage_in_argument():
    """Test usage of Isolated objects as function arguments."""

    def qux(a, b=Isolated(), c=Evaluated(lambda: 42), d=43):
        return a, b, c, d

    smart_qux = smart_args(qux)
    isolated_obj = object()
    assert smart_qux(1, b=isolated_obj) == (1, isolated_obj, 42, 43)


def test_mixed_evaluated_and_isolated_in_same_argument():
    """Test that mixing Evaluated and Isolated in one argument fails."""

    def fizz(a, b=Isolated(), c=Evaluated(lambda: 42)):
        return a, b, c

    smart_fizz = smart_args(fizz)
    with pytest.raises(ValueError):
        smart_fizz(1, b=object())


def test_missing_required_isolated_arg():
    """Test that missing an Isolated argument with no default value raises an error."""

    def buzz(a, b=Isolated(), c=Evaluated(lambda: 42)):
        return a, b, c

    smart_buzz = smart_args(buzz)
    with pytest.raises(ValueError):
        smart_buzz(1)


def test_evaluated_overridden_by_passed_value():
    """Test that passing an argument overrides the Evaluated default."""

    def blizz(a, b=Evaluated(lambda: 42)):
        return a, b

    smart_blizz = smart_args(blizz)
    assert smart_blizz(1, b=33) == (1, 33)


def test_bad_isolated_use_no_value():
    """Test that using Isolated without providing a value raises an error."""

    def zap(a, b=Isolated()):
        return a, b

    smart_zap = smart_args(zap)
    with pytest.raises(ValueError):
        smart_zap(1)


def test_bad_usage_of_evaluated_and_isolated():
    """Test that mixing Evaluated and Isolated in the wrong way fails."""

    def poof(a, b=Isolated(), c=Evaluated(lambda: 42)):
        return a, b, c

    smart_poof = smart_args(poof)
    with pytest.raises(ValueError):
        smart_poof(1, b=object(), c=object())


def test_multiple_isolated_objects():
    """Test that multiple Isolated objects can be used correctly."""

    def pow(a, b=Isolated(), c=Isolated()):
        return a, b, c

    smart_pow = smart_args(pow)
    obj1 = object()
    obj2 = object()
    assert smart_pow(1, b=obj1, c=obj2) == (1, obj1, obj2)


def test_recursive_use_of_evaluated_and_isolated():
    """Test that recursive usage of Evaluated and Isolated works."""

    def foobar(a, b=Isolated(), c=Evaluated(lambda: 42), d=Evaluated(lambda: foobar(3, b=Isolated()))):
        return a, b, c, d

    smart_foobar = smart_args(foobar)
    obj = object()
    assert smart_foobar(1, b=obj) == (1, obj, 42, foobar(3, b=obj))


def test_correct_argument_order():
    """Test that arguments are handled in the right order even with defaults."""

    def boom(a, b=Isolated(), c=Evaluated(lambda: 42)):
        return a, b, c

    smart_boom = smart_args(boom)
    obj = object()
    assert smart_boom(1, b=obj, c=43) == (1, obj, 43)


def test_nested_evaluated_and_isolated():
    """Test that nested usage of Evaluated and Isolated still works."""

    def kerplunk(a, b=Isolated(), c=Evaluated(lambda: 42), d=Evaluated(lambda: kerplunk(3, b=Isolated()))):
        return a, b, c, d

    smart_kerplunk = smart_args(kerplunk)
    obj = object()
    assert smart_kerplunk(1, b=obj) == (1, obj, 42, kerplunk(3, b=obj))


def test_chaining_evaluated_and_isolated():
    """Test that chaining evaluations and isolations still works."""

    def doop(a, b=Isolated(), c=Evaluated(lambda: 42), d=Evaluated(lambda: doop(3, b=Isolated()))):
        return a, b, c, d

    smart_doop = smart_args(doop)
    obj = object()
    assert smart_doop(1, b=obj) == (1, obj, 42, doop(3, b=obj))


def test_combination_of_evaluated_and_isolated():
    """Test that combining both types of arguments works correctly."""

    def kaboom(a, b=Isolated(), c=Evaluated(lambda: 42), d=Evaluated(lambda: kaboom(3, b=Isolated()))):
        return a, b, c, d

    smart_kaboom = smart_args(kaboom)
    obj = object()
    assert smart_kaboom(1, b=obj) == (1, obj, 42, kaboom(3, b=obj))


def test_overriding_nested_evaluated_and_isolated():
    """Test that overriding nested evaluation and isolation works correctly."""

    def kludge(a, b=Isolated(), c=Evaluated(lambda: 42), d=Evaluated(lambda: kludge(3, b=Isolated()))):
        return a, b, c, d

    smart_kludge = smart_args(kludge)
    obj = object()
    assert smart_kludge(1, b=obj, d=77) == (1, obj, 42, 77)


def test_evaluted_override_nested_evaluated():
    """Test that evaluating overrides nested evaluations."""

    def bang(a, b=Isolated(), c=Evaluated(lambda: 42), d=Evaluated(lambda: bang(3, b=Isolated()))):
        return a, b, c, d

    smart_bang = smart_args(bang)
    obj = object()
    assert smart_bang(1, b=obj, d=77) == (1, obj, 42, 77)