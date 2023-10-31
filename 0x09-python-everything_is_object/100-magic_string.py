#!/usr/bin/python3
def magic_string():
    magic_string.add = getattr(magic_string, "add", 0) + 1
    return ", ".join(["BestSchool" for _ in range(magic_string.add)])
