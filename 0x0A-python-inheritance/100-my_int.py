#!/usr/bin/python3
"""Module"""


class MyInt (int):
    """class my int"""

    def __eq__(self, other):
        """function la"""

        return (int(self) != other)

    def __ne__(self, other):
        """function ne"""

        return int(self) == other
