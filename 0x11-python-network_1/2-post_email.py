#!/usr/bin/python3
"""MODULES"""
import urllib.request as reqa
import urllib as ur
from sys import argv as ar

def fun():
    try:
        with reqa.urlopen(reqa.Request(ar[1], ur.parse.urlencode({"email": ar[2]}).encode('ascii'))) as lal:
            print(lal.read().decode('utf-8'))
    except:
        pass
        
if __name__ == "__main__":
    fun()
