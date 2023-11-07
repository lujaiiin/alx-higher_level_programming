#!/usr/bin/python3
"""Module"""
import sys
haf = __import__("5-save_to_json_file").save_to_json_file
tah = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
listn = list(sys.argv[1:])
try:
    lib = tah(filename)
except Exception:
    lib = []
lib.extend(listn)
haf(lib, filename)
