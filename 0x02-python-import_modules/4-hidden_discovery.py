#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    prio = dir(hidden_4)
    for i in prio:
        if i[:2] != "__":
            print(i)
