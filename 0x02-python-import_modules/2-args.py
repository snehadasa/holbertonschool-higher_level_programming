#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_av = len(argv) - 1
    if num_av == 0:
        print("{} arguments.".format(num_av))
    elif num_av == 1:
        print("{} argument:".format(num_av))
    else:
        print("{} arguments:".format(num_av))
    if num_av > 0:
        for i in range(1, num_av + 1):
            print("{:d}: {}".format(i, argv[i]))
