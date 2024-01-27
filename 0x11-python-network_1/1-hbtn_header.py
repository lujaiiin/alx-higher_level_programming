#!/usr/bin/python3
"""Modules"""
import urllib.request
from sys import argv as ar


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(ar[1]) as URLVA:
            RS = URLVA.info()
            print(RS['X-Request-Id'])
    except:
        pass
