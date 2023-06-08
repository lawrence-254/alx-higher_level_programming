#!/usr/bin/python3

import sys

if __name__ == "__main__":
    ac = 0
    for i in range(1, len(sys.argv)):
        ac += int(sys.argv[i])
    print("{}".format(ac))
