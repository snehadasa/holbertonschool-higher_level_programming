#!/usr/bin/python3

def trim_spaces(string):
    i = 0
    for j in range(len(string)):
        if string[j] == " ":
            i = i+1
        else:
            break
    print(string[i:], end="")

def text_indentation(text):
    lst = text.replace('.','.@#$').replace('?','?@#$').replace(':',':@#$').split('@#$')
    for st in lst[:-1]:
        trim_spaces(st)
        print("")
        print("")
    trim_spaces(lst[-1])
