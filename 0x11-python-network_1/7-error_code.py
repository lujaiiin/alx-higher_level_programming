#!/usr/bin/python3
"""MODULES"""
from sys import argv as ar
import requests as re

def fun():
    try:
        if re.get(ar[1]).status_code >= 400:
            print("Error code: {}".format(re.get(ar[1]).status_code))
        else:
            print(re.get(ar[1]).text)
    except:
        pass
        
if __name__ == "__main__":
    fun()
