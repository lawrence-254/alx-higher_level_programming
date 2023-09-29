#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as result:
            content = result.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except Exception:
        pass
