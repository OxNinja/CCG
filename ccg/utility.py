import validators


def is_slug(text: str) -> bool:
    """Returns if a given str is in a slug format

    :param text: The string to test
    :type text: str
    :return: `True` if the given text is in a slug format, `False` else
    :rtype: bool
    """
    if not validators.slug(text):
        return False
    else:
        return True