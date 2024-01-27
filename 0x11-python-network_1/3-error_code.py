#!/usr/bin/python3
"""Modules"""
from urllib.error import HTTPError
from sys import argv as ar
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(ar[1]) as URLVA:
            VALf = URLVA.read()
            print(VALf.decode('UTF-8'))
    except HTTPError as ERROR:
        print('Error code:', ERROR.code)
    except:
        pass
