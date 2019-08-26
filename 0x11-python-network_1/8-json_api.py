#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
   the body of the response.
"""


import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    try:
        req = requests.post('http://0.0.0.0:5000/search_user',
                           data={'q': q}).json()
        if 'id' in req and 'name' in req:
            print("[{}] {}".format(req['id'], req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
