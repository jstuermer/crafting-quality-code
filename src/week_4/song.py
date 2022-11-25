class Song:
    """
    A song class.

    Parameters
    ----------
    artist : str
        The name of the artist of the song.
    title : str
        The title of the song.
    minutes : int
        The minutes of the song duration.
    seconds : int
        The seconds of the song duration.

    Examples
    --------
    >>> song = Song("Neil Young", "Harvest Moon", 5, 3)
    >>> song.artist
    'Neil Young'
    >>> song.title
    'Harvest Moon'
    >>> song.minutes
    5
    >>> song.seconds
    3
    """

    def __init__(self, artist: str, title: str, minutes: int, seconds: int) -> None:
        self.artist = artist
        self.title = title
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        """
        Return a string representation of this song.

        Examples
        --------
        >>> song = Song("Neil Young", "Harvest Moon", 5, 3)
        >>> str(song)
        'Harvest Moon by Neil Young (5:03)'
        """

        return "%s by %s (%d:%s)" %(
            self.title, self.artist, self.minutes, str(self.seconds).rjust(2, "0")
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()