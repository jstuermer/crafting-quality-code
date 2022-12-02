# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """
    A rat caught in a maze.

    Parameters
    ----------
    symbol : str
        The symbol that represents the rat in a maze. Has to be a string of length 1.
    row : int
        The row index of the rat's location in the maze.
    col : int
        The column index of the rat's location in the maze.
    num_sprouts_eaten : int
        Counts the number of sprouts eaten by the rat. Initialized as 0.

    Examples
    --------
    >>> paul = Rat("P", 1, 4)
    >>> paul.symbol
    'P'
    >>> paul.row
    1
    >>> paul.col
    4
    >>> paul.num_sprouts_eaten
    0
    """

    def __init__(self, symbol: str, row: int, col: int) -> None:
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row: int, col: int) -> None:
        """
        Set the location of the rat to row `row` and column `col`.

        Parameters
        ----------
        row : int
            The row index to be set as the rat's location in the maze.
        col : int
            The column index to be set as the rat's location in the maze.

        Examples
        --------
        >>> paul = Rat("P", 1, 4)
        >>> (paul.row, paul.col)
        (1, 4)
        >>> paul.set_location(2, 3)
        >>> (paul.row, paul.col)
        (2, 3)
        """

        self.row = row
        self.col = col

    def eat_sprout(self) -> None:
        """
        Increase the number of sprouts eaten by the rat by 1.

        Examples
        --------
        >>> paul = Rat("P", 1, 4)
        >>> paul.num_sprouts_eaten
        0
        >>> paul.eat_sprout()
        >>> paul.num_sprouts_eaten
        1
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        Return a string representation of the rat.

        Examples
        --------
        >>> paul = Rat("P", 1, 4)
        >>> str(paul)
        'P at (1, 4) ate 0 sprouts.'
        """

        return "%s at (%d, %d) ate %d sprouts." %(
            self.symbol, self.row, self.col, self.num_sprouts_eaten
        )

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.