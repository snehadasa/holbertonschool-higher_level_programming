#!/usr/bin/python3
"""Python script that takes in a string and sends a search request to the
   Star Wars API"""


import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if 'id' in req:
        print(req['id'])
    else:
        print(None)
