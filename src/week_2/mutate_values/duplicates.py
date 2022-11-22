def remove_shared(L1, L2):
    """
    Remove items from list L1 that are both in L1 and L2.

    Parameters
    ----------
    L1 : list
        The list to potentially remove items from.
    L2 : list
        The list containing items to remove in L1.

    Returns
    -------
    None
        The result is the mutated version of L1.

    Examples
    --------
    >>> list_1 = [1, 2, 3, 4, 5, 6]
    >>> list_2 = [2, 4, 5, 7]
    >>> remove_shared(list_1, list_2)
    >>> list_1
    [1, 3, 6]
    >>> list_2
    [2, 4, 5, 7]
    """

    for v in L2:
        if v in L1:
            L1.remove(v)

if __name__ == '__main__':
    import doctest
    doctest.testmod()