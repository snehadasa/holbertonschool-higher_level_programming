#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = 0
    try:
        res = fct(*args)
        return res
    except Exception as fmt:
        print("Exception: {}".format(fmt), file=sys.stderr)
        return None
