#!/usr/bin/python3
"""MODULES"""
import requests as re
from sys import argv as ar


def fun():
    try:
        lala = re.get("https://api.github.com/repos/{}/{}/commits".format(ar[2], ar[1]), params={"per_page": 10}, headers={"X-GitHub-Api-Version": "2022-11-28"}).json()
        for co in lala:
            print("{}: {}".format(co.get("sha"),
                                co.get("commit").get("author").get("name")))
    except:
        pass
    
if __name__ == "__main__":
    fun()
