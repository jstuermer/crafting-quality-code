def bubble_sort(L: list) -> None:
    """
    Sort the items in L from smallest to largest integer.

    Parameters
    ----------
    L : list[int]
        The list to be sorted.

    Examples
    --------
    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    end = len(L) - 1

    while end > 0:
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]

        end -= 1


def get_index_of_smallest(L: list) -> int:
    """
    Return the index of the smallest value in L.

    Parameters
    ----------
    L : list[int]
        The list to be considered.

    Returns
    -------
    int
        The index of the smallest value.

    Examples
    --------
    >>> get_index_of_smallest([3, 4, 2, 7])
    2

    >>> get_index_of_smallest([1, 2])
    0

    >>> get_index_of_smallest([3, 2, 2, 4])
    1
    """

    n = len(L)
    index_of_smallest = 0
    for i in range(n):
        if L[i] < L[index_of_smallest]:
            index_of_smallest = i

    return index_of_smallest


def selection_sort(L: list) -> None:
    """
    Sort the items in L from smallest to largest integer.

    Parameters
    ----------
    L : list[int]
        The list to be sorted.

    Examples
    --------
    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    for i in range(len(L)):
        index_of_smallest = get_index_of_smallest(L[i:])
        L[i], L[index_of_smallest] = L[index_of_smallest], L[i]


def insert(L: list, i: int) -> None:
    """
    Precondition: L[:i] is sorted from smallest value to largest.

    Insert the value L[i] into the preceding sorted list L[:i] such that L[:i+1]
    is sorted afterwards.

    Parameters
    ----------
    L : list[int]
        The list of integers to consider.
    i : int
        The index of L[i] which is to be inserted into L[:i].

    Examples
    --------
    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """

    value = L[i]  # the value to insert into L[:i]
    j = i

    while j > 0 and value < L[j - 1]:
        L[j] = L[j - 1]  # shift larger values to the right
        j -= 1

    L[j] = value  # insert L[i] at the right place


def insertion_sort(L: list) -> None:
    """
    Sort the items in L from smallest to largest integer.

    Parameters
    ----------
    L : list[int]
        The list to be sorted.

    Examples
    --------
    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    n = len(L)
    for i in range(1, n):
        insert(L, i)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
