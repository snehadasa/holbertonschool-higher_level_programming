#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the
   passed URL with the email as a parameter, and displays the body of the
   response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res = response.read()
    print(res.decode("utf-8"))
