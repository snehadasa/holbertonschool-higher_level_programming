#!/usr/bin/python3
"""module to read the file and print the lines read"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as myFile:
        if nb_lines <= 0:
            s = myFile.read()
            print(s, end="")
        else:
            for line in myFile:
                if (nb_lines != 0):
                    print(line, end="")
                    nb_lines -= 1
