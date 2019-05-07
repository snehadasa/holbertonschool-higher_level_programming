#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(sum(i) for i in zip (tuple_a, tuple_b))
