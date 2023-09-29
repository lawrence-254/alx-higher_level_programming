#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    content = requests.get(url)
    if content is not None:
        print("Body response:")
        print("\t- type: {}".format(type(content.text)))
        print("\t- content: {}".format(content.text))
