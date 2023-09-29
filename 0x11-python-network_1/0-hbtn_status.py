#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as result:
            content = result.read()
            print("Body response:$")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")
    except Exception:
        pass
