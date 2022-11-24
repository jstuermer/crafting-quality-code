class CashRegister:
    """
    A cash register that stores the number and type of dollar bills.

    Parameters
    ----------
    ones : int
        The number of one-dollar bills.
    twos : int
        The number of two-dollar bills
    fives : int
        The number of five-dollar bills.
    tens : int
        The number of ten-dollar bills.
    twenties : int
        The number of twenty-dollar bills.

    Examples
    --------
    >>> register = CashRegister(1, 2, 3, 4, 5)
    >>> register.ones
    1
    >>> register.twos
    2
    >>> register.fives
    3
    >>> register.tens
    4
    >>> register.twenties
    5
    """

    def __init__(
        self,
        ones: int,
        twos:int,
        fives: int,
        tens: int,
        twenties: int
    ) -> None:
        """Initialize a register."""

        self.ones = ones
        self.twos = twos
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def get_total(self) -> int:
        """
        Return the total amount of cash stored in the register.

        Examples
        --------
        >>> register = CashRegister(1, 2, 3, 4, 5)
        >>> register.get_total()
        160
        """

        return (
            self.ones
            + 2 * self.twos
            + 5 * self.fives
            + 10 * self.tens
            + 20 * self.twenties
        )

    def add(self, amount: int, denomination: str) -> None:
        """
        Add amount items of denomination to the register.

        Parameters
        ----------
        amount : int
            The amount to add to the register.
        denomination : str
            The type of bill to add ("ones", "twos", "fives", "tens" or "twenties").

        Examples
        --------
        >>> register = CashRegister(1, 2, 3, 4, 5)
        >>> register.add(2, "ones")
        >>> register.ones
        3
        >>> register.add(1, "tens")
        >>> register.tens
        5
        """

        self.__dict__[denomination] += amount

    def remove(self, amount: int, denomination: str) -> None:
        """
        Remove amount items of denomination from the register.

        Parameters
        ----------
        amount : int
            The amount to remove from the register.
        denomination : str
            The type of bill to remove ("ones", "twos", "fives", "tens" or "twenties").

        Examples
        --------
        >>> register = CashRegister(1, 2, 3, 4, 5)
        >>> register.remove(1, "ones")
        >>> register.ones
        0
        >>> register.remove(2, "tens")
        >>> register.tens
        2
        """

        self.__dict__[denomination] -= amount

if __name__ == "__main__":
    import doctest

    doctest.testmod()