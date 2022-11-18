def is_palindrome_v2(s):
    """ (str) -> (bool)

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2("noon")
    True
    >>> is_palindrome_v2("racecar")
    True
    >>> is_palindrome_v2("dented")
    False
    """

    s_first_half, s_second_half = split(s)

    return reverse(s_second_half) == s_first_half

def split(s):
    """ (str) -> (str, str)

    Return the first and second half of s. The middle character of an odd-length
    string is omitted.

    >>> split("noon")
    ("no", "on")
    >>> split("racecar")
    ("rac", "car")
    >>> split("dented")
    ("den", "ted")
    >>> split("a")
    ("", "")
    """

    halves_len = len(s) // 2

    return s[:halves_len], s[len(s) - halves_len:]

def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse("hello")
    "olleh"
    >>> reverse("a")
    "a"
    """

    s_reversed = ""
    for char in s:
        s_reversed = char + s_reversed

    return s_reversed
