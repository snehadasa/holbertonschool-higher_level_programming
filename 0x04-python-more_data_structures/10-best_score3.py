#!/usr/bin/python3
def best_score(a_dictionary):
    r = 0
    for r in a_dictionary:
        r = sorted(a_dictionary.keys(), key = (lambda k: a_dictionary[k]))
        return (r[-1])
