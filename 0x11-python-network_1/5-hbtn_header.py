#!/usr/bin/python3
'''a Python script that takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.'''
import requests
import sys


if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    x_id = result.headers.get("X-Request-Id")

    if x_id:
        print(x_id)
