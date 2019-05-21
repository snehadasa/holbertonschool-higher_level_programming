#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            result += 1
    except:
        pass
    print("")
    return result
