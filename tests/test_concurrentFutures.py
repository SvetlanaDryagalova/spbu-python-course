import pytest
from project.concurrentFutures import product_sum, cartesian_product_sum


def test_product_sum():
    # test for product_sum
    assert product_sum([1, 2, 3]) == 6
    assert product_sum([-1, 1]) == 0
    assert product_sum([0, 0, 0]) == 0


def test_cartesian_product_sum():
    # test for cartesian_product_sum
    assert cartesian_product_sum([1, 2]) == 12
    assert cartesian_product_sum([0, 2]) == 8
    assert cartesian_product_sum([5, 7]) == 48

    # test with empty list
    with pytest.raises(ValueError):
        cartesian_product_sum([])

    # test with None
    with pytest.raises(ValueError):
        cartesian_product_sum(None)
