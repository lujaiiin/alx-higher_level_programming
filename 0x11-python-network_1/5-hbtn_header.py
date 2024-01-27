#!/usr/bin/python3
""" print the id found in headers """
import requests as re
from sys import argv as ar

def fun():
    print(re.get(ar[1]).headers.get("X-Request-Id"))
    
if __name__ == "__main__":
    fun()
