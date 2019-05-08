#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += [0, 0]
    tuple_b += [0, 0]
    add_max = tuple_a[0] + tuple_b[0]
    add_min = tuple_a[1] + tuple_b[1]
    return (add_max, add_min)
