#!/usr/bin/python3
def magic_string():
    return "$".join(["BestSchool" * (i + 1) for i in range(10)]) + "$"
