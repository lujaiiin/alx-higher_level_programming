#!/usr/bin/python3
"""MODULES"""
import requests
from sys import argv as ar


def fun():
    try:
        de = {'email': ar[2]}
        print(requests.post(ar[1], data=de).text)
    except:
        pass
    
if __name__ == "__main__":
    fun()
