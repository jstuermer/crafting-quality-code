import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(0)
    0
    >>> num_buses(1)
    1
    >>> num_buses(50)
    1
    >>> num_buses(75)
    2
    >>> num_buses(100)
    2
    >>> num_buses(101)
    3
    """

    people_per_bus = 50

    return math.ceil(n / people_per_bus)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([])
    (0.0, 0.0)
    >>> stock_price_summary([0, 0.0, 0.0])
    (0.0, 0.0)
    >>> stock_price_summary([-1.2, -5.3])
    (0.0, -6.5)
    >>> stock_price_summary([1.2, 5.3])
    (6.5, 0.0)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    gains = [pc for pc in price_changes if pc > 0.0]
    losses = [pc for pc in price_changes if pc < 0.0]

    return math.fsum(gains), math.fsum(losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondition: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = []
    >>> swap_k(nums, 0)
    >>> nums
    []
    >>> nums = [1]
    >>> swap_k(nums, 0)
    >>> nums
    [1]
    >>> nums = [1, 2]
    >>> swap_k(nums, 0)
    >>> nums
    [1, 2]
    >>> nums = [1, 2]
    >>> swap_k(nums, 1)
    >>> nums
    [2, 1]
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    L_copy = L.copy()
    for i in range(k):
        L[i] = L_copy[-k+i]
        L[-k+i] = L_copy[i]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
