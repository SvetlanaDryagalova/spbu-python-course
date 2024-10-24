import concurrent.futures
import itertools


def product_sum(numbers: list[int]) -> int:
    """
        Calculates the sum of the numbers in the input list.
        Parameters
            numbers : list[int]
                The list of numbers.
        Returns
            sum : int
                The sum of numbers.
    """
    return sum(numbers)


def cartesian_product_sum(numbers: list[int]) -> int:
    """
        Calculates sum of Cartesian product of the numbers in the input list.
        Parameters
            numbers : list[int]
                The list of numbers.
        Returns
            total_sum : int
                The result of sum of the Cartesian product of numbers.
        Raises
            ValueError
                If the input list of numbers is empty.
    """
    if numbers is None or numbers == []:
        raise ValueError('List must not be empty!')

    product = list(itertools.product(numbers, repeat=2))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(product_sum, product))

    total_sum = sum(results)

    return total_sum
