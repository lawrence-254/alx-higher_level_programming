#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL
"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    try:
        with urllib.request.urlopen(req) as resp:
            if resp is not None:
                html = resp.read()
                print(html.decode('utf-8'))
    except Exception:
        pass
