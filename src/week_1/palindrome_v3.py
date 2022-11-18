def is_palindrome_v3(s):
    """ (str) -> (bool)

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v3("noon")
    True
    >>> is_palindrome_v3("racecar")
    True
    >>> is_palindrome_v3("dented")
    False
    """

    for i in range(0, len(s)//2):
        if s[i] != s[-(i+1)]:
            return False

    return True