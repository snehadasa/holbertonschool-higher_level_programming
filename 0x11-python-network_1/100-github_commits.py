#!/usr/bin/python3
"""Python script that takes in a string and sends a search request to the
   Star Wars API"""


import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get('https://api.github.com/repos/{}/{}/commits/'
                       .format(argv[2], argv[1])).json()
    c = 0
    for ar in req:
        if c == 10:
            break
        try:
            name = ar.get("commit").get("author").get("name")
            sha = ar.get("sha")
            print("{}: {}".format(sha, name))
            c += 1
        except AttributeError:
            pass
