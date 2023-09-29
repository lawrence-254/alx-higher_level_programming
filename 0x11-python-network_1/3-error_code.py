#!/usr/bin/python3
'''displays the body of the response (decoded in utf-8).'''
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as result:
            content = result.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    except urllib.error.URLError as e:
        print('Url Error: {}'.format(e.reason))
