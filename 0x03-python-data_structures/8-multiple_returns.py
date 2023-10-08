#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        lengh = len(sentence)
        val = sentence[0]
    else:
        lengh = len(sentence)
        val = None
    return lengh, val
