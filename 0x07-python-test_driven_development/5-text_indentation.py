#!/usr/bin/python3
"""Module."""

def text_indentation(text):
    """text function to print split string"""

    if type(text) != str:
        raise TypeError('text must be a string')
    text = text.strip()
    res = ""
    for i in text:
        res += i
        if i in [".", "?", ":"]:
            res += "\n\n"
    print(res)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
