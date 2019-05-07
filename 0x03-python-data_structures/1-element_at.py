#!/usr/bin/python3
def element_at(my_list, idx):
    total_len = len(my_list)
    if idx < 0:
        return None
    elif idx > total_len:
        return None
    else:
        return my_list[idx]
