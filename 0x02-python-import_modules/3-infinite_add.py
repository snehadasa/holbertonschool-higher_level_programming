#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_argv = len(sys.argv) - 1
    add_argv = 0
    if sum_argv > 0:
        for i in range(len(sys.argv)):
            if i > 0:
                add_argv += int(sys.argv[i])
    print("{}".format(add_argv))
