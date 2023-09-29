#!/usr/bin/python3
'''a Python script that takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.'''
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as result:
    x_request_id = result.getheader("X-Request-Id")
    if x_request_id:
        print(x_request_id)
