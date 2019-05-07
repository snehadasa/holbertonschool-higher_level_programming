#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        sentence = None
    str_len = len(tuple(sentence))
    first = sentence[0]
    return (str_len, first)
