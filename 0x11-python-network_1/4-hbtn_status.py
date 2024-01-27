#!/usr/bin/python3
"""MODULES"""
import requests as ra


def fun():
    try:
        re = ra.get('https://alx-intranet.hbtn.io/status')
        co = re.text
        print("Body response:")
        print("\t- type: {}".format(type(co)))
        print("\t- content: {}".format(co))
    except:
        pass
        
if __name__ == "__main__":
    fun()
