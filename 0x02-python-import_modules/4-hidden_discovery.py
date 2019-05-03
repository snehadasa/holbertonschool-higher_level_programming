#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in names:
        if names[0:2] != '__':
            print(i)
