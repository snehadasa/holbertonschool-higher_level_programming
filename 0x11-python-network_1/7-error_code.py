#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
   the body of the response.
"""


import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    code = req.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(req.text)
