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

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
