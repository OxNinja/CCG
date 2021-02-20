import string
import sys
import validators
from os.path import exists, isfile


def is_slug(text: str) -> bool:
    """Returns if a given str is in a slug format

    :param text: The string to test
    :type text: str
    :return: `True` if the given text is in a slug format, `False` else
    :rtype: bool
    """
    if not validators.slug(text):
        return False
    return True


def rot_n(string: str, shift: int) -> str:
    """Shifts the given string by an amount of `shift` characters (see rot13 or rot26 for example)

    :param string: The string to shift
    :param shift: The amount to shift the given string
    """
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    result = ''
    for char in string:
        if char in upper:
            result += upper[(upper.index(char) + shift) % len(upper)]
        elif char in lower:
            result += lower[(lower.index(char) + shift) % len(lower)]
        else:
            result += char
    return result


def file_write(data: str, path: str) -> None:
    """Rewrites the content of file `path` with `data`

    :param data: The content to write
    :param path: The path of the file
    """

    # TODO: Check if the given path is valid

    with open(path, "w") as file_:
        file_.write(data)
