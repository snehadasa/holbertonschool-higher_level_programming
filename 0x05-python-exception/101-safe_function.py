#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as fmt:
        print("Exception: {}".format(fmt), file=sys.stderr)
        return None
