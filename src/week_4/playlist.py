import song

class Playlist:
    """
    A playlist of songs.

    Parameters
    ----------
    title : str
        The title of the playlist.
    songs : List[Song]
        A list of songs that stores which songs have been added to the playlist.

    Examples
    --------
    >>> playlist = Playlist("Canadian Artists")
    >>> playlist.title
    'Canadian Artists'
    >>> playlist.songs
    []
    """

    def __init__(self, title: str) -> None:
        self.title = title
        self.songs = []

    def __str__(self):
        """
        Return a string representation of this playlist.

        Examples
        --------
        >>> playlist = Playlist("Canadian Artists")
        >>> playlist.add(song.Song("Serena Ryder", "Stompa", 3, 15))
        >>> playlist.add(song.Song("Neil Young", "Harvest Moon", 5, 3))
        >>> print(playlist)
        Playlist: Canadian Artists (8:18)
        1. Stompa by Serena Ryder (3:15)
        2. Harvest Moon by Neil Young (5:03)
        """

        total_duration = self.get_duration()
        total_minutes = str(total_duration[0])
        total_seconds = str(total_duration[1]).rjust(2, "0")

        s = "Playlist: %s (%s:%s)" %(self.title, total_minutes, total_seconds)
        song_num = 1
        for song in self.songs:
            s += "\n" "%d. "%(song_num) + str(song)
            song_num += 1

        return s

    def add(self, song: song.Song) -> None:
        """
        Add song to this playlist.

        Parameters
        ----------
        song : song.Song
            The song to add to the playlist.

        Examples
        --------
        >>> stompa = song.Song("Serena Ryder", "Stompa", 3, 15)
        >>> playlist = Playlist("My Playlist")
        >>> playlist.add(stompa)
        >>> playlist.songs[0] == stompa
        True
        """

        self.songs.append(song)

    def get_duration(self) -> tuple:
        """
        Return the total duration of this playlist.

        Examples
        --------
        >>> playlist = Playlist("Canadian Artists")
        >>> playlist.add(song.Song("Serena Ryder", "Stompa", 3, 15))
        >>> playlist.add(song.Song("Neil Young", "Harvest Moon", 5, 3))
        >>> playlist.get_duration()
        (8, 18)
        """

        total_minutes = 0
        total_seconds = 0
        for song in self.songs:
            total_minutes += song.minutes
            total_seconds += song.seconds

        return total_minutes + total_seconds // 60, total_seconds % 60


if __name__ == "__main__":
    import doctest

    doctest.testmod()