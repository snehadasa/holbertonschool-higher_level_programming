#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = 0
    second = 0
    if len(tuple_a) > 0:
        first += tuple_a[0]
    if len(tuple_a) > 1:
        second += tuple_a[1]
    if len(tuple_b) > 0:
        first += tuple_b[0]
    if len(tuple_b) > 1:
        second += tuple_b[1]
    return (first, second)
