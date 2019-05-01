#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ""
        if ord(i) >= 97 and ord(i) <= 122:
            c = ord(i) - 32
        else:
            c = ord(i)
        print("{:c}".format(c), end="")
    print("")
