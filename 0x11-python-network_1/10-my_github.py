#!/usr/bin/python3
"""MODULES """
import requests as re
from sys import argv as ar
from requests.auth import HTTPBasicAuth


def fun():
    try:
        if '{' and '}' in re.get("https://api.github.com/user", auth=HTTPBasicAuth(ar[1], ar[2]), headers={"X-GitHub-Api-Version": "2022-11-28"}).text:
            print(re.get("https://api.github.com/user", auth=HTTPBasicAuth(ar[1], ar[2]), headers={"X-GitHub-Api-Version": "2022-11-28"}).json().get("id"))
        else:
            print(None)
    except:
        pass
    
if __name__ == "__main__":
    fun()
