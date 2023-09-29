#!/usr/bin/python3
'''displays the body of the response (decoded in utf-8).'''
import requests
import sys


if __name__ == "__main__":
    result = requests.get(sys.argv[1])
    if result:
        if result.status_code >= 400:
            print('Error code: {}'.format(result.status_code))
        else:
            print(result.text)
