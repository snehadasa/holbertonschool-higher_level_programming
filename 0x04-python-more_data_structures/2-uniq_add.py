#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_set = set(my_list)
    unique_list = list(list_set)
    sum_list = sum(unique_list)
    return sum_list
