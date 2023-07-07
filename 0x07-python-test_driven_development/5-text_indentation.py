#!/usr/bin/python3
"""Prints a text with 2 new lines after each character"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): text to be printed

    Raises:
        TypeError: If the input text is not a string

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text.strip() == "":
        return

    res = []
    curr_line = ""
    for char in text:
        curr_line += char
        if char in (".", "?", ":"):
            res.append(curr_line.strip())
            res.append("")
            curr_line = ""

    if curr_line:
        res.append(curr_line.strip())

    print("\n".join(res))
