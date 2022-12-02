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
    >>> paul = Rat('P', 1, 4)
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
        if len(symbol) != 1:
            raise(
                ValueError,
                "symbol contains %d characters instead of one." %(len(symbol))
            )

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
        >>> paul = Rat('P', 1, 4)
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
        >>> paul = Rat('P', 1, 4)
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
        >>> paul = Rat('P', 1, 4)
        >>> str(paul)
        'P at (1, 4) ate 0 sprouts.'
        """

        return "%s at (%d, %d) ate %d sprouts." %(
            self.symbol, self.row, self.col, self.num_sprouts_eaten
        )

class Maze:
    """
    A 2D maze that can contain two rats and various sprouts.

    Parameters
    ----------
    contents : List[List[str]]
        A 2D list of the contents present in the maze. Each item should be a str of
        length 1.
    rat_1 : Rat
        The first rat in the maze.
    rat_2 : Rat
        The second rat in the maze.
    num_sprouts_left : int
        The number of sprouts left in the maze.

    Examples
    --------
    >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
    ...              ['#', '.', '.', '.', '.', '.', '#'],
    ...              ['#', '.', '#', '#', '#', '.', '#'],
    ...              ['#', '.', '.', '@', '#', '.', '#'],
    ...              ['#', '@', '#', '.', '@', '.', '#'],
    ...              ['#', '#', '#', '#', '#', '#', '#']],
    ...              Rat('J', 1, 1),
    ...              Rat('P', 1, 4))
    >>> str(maze.rat_1)
    'J at (1, 1) ate 0 sprouts.'
    >>> str(maze.rat_2)
    'P at (1, 4) ate 0 sprouts.'
    >>> maze.num_sprouts_left
    3
    """

    def __init__(self, contents: list, rat_1: Rat, rat_2: Rat) -> None:
        self.contents = contents
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sum(l.count(SPROUT) for l in self.contents[1:-1])

    def is_wall(self, row: int, col: int) -> bool:
        """
        Return `True` if and only if there is a wall at the given row and column of the
        maze.

        Parameters
        ----------
        row : int
            The row index of the considered location.
        col : int
            The column index of the considered location.

        Examples
        --------
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...              Rat('J', 1, 1),
        ...              Rat('P', 1, 4))
        >>> maze.is_wall(1, 0)
        True
        >>> maze.is_wall(1, 1)
        False
        """

        return self.contents[row][col] == WALL

    def get_character(self, row: int, col: int) -> str:
        """
        Return the character in the maze at the specified row and column. If there is a
        rat at the given location, its `symbol` parameter is returned.

        Parameters
        ----------
        row : int
            The row index of the considered location.
        col : int
            The column index of the considered location.

        Examples
        --------
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...              Rat('J', 1, 1),
        ...              Rat('P', 1, 4))
        >>> maze.get_character(0, 2)
        '#'
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.get_character(1, 4)
        'P'
        >>> maze.get_character(3, 3)
        '@'
        """

        if (self.rat_1.row, self.rat_1.col) == (row, col):
            return self.rat_1.symbol

        if (self.rat_2.row, self.rat_2.col) == (row, col):
            return self.rat_2.symbol

        return self.contents[row][col]

    def move(self, rat: Rat, vertical_change: str, horizontal_change: str) -> bool:
        """
        Move the rat in the given direction, unless there is a wall in the way.

        If the character at the new location is a sprout, the rat eats it according to
        `Rat.eat_sprout`. The sprout character in `maze.contents` is then replaced with
        a `HALL`.

        Parameters
        ----------
        rat : Rat
            The rat to move.
        vertical_change : int, UP, NO_CHANGE, or DOWN
            The change in the vertical direction.
        horizontal_change : int, LEFT, NO_CHANGE or RIGHT
            The change in the horizontal direction.

        Returns
        -------
        bool
            Return True if and only if the there was no wall in the way, i.e., the rat
            was moved successfully.

        Examples
        --------
        >>> jen = Rat('J', 1, 1)
        >>> paul = Rat('P', 1, 4)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...              jen,
        ...              paul)
        >>> maze.move(jen, UP, NO_CHANGE)
        False
        >>> str(jen)
        'J at (1, 1) ate 0 sprouts.'
        >>> maze.move(paul, NO_CHANGE, LEFT)
        True
        >>> str(paul)
        'P at (1, 3) ate 0 sprouts.'
        >>> jen.set_location(3, 2)
        >>> maze.move(jen, NO_CHANGE, RIGHT)
        True
        >>> str(jen)
        'J at (3, 3) ate 1 sprouts.'
        """

        new_row = rat.row + vertical_change
        new_col = rat.col + horizontal_change

        if self.get_character(new_row, new_col) == WALL:
            return False

        if self.get_character(new_row, new_col) == SPROUT:
            self.contents[new_row][new_col] = HALL
            rat.num_sprouts_eaten += 1

        rat.set_location(new_row, new_col)
        return True

    def __str__(self) -> str:
        """
        Return a string representation of the maze.

        Examples
        --------
        >>> jen = Rat('J', 1, 1)
        >>> paul = Rat('P', 1, 4)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'],
        ...              ['#', '.', '.', '.', '.', '.', '#'],
        ...              ['#', '.', '#', '#', '#', '.', '#'],
        ...              ['#', '.', '.', '@', '#', '.', '#'],
        ...              ['#', '@', '#', '.', '@', '.', '#'],
        ...              ['#', '#', '#', '#', '#', '#', '#']],
        ...              jen,
        ...              paul)
        >>> print(maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        s = ''
        for (row, row_contents) in enumerate(self.contents):
            if self.rat_1.row == row:
                row_contents[self.rat_1.col] = self.rat_1.symbol
            if self.rat_2.row == row:
                row_contents[self.rat_2.col] = self.rat_2.symbol
            s += ''.join(row_contents) + '\n'

        s += str(self.rat_1) + '\n' + str(self.rat_2)

        return s