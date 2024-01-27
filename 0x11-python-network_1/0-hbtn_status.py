#!/usr/bin/python3
"""Modules"""
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as URL:
            val = URL.read()
            print("Body response:")
            print("\t- type: {}".format(type(val)))
            print("\t- content: {}".format(val))
            print("\t- utf8 content: {}".format(val.decode("UTF-8")))
    except:
        pass
