#!/usr/bin/python3
"""Python script that takes in a string and sends a search request to the
   Star Wars API"""


import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get('https://swapi.co/api/people/?search={}'
                       .format(argv[1]))
    print("Number of results: {}".format(req.json()["count"]))
    for res in req.json()["results"]:
        print(res["name"])
