#!/usr/bin/python3
'''finds a peak in a list of unsorted integers'''


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        mid = (start + end) // 2
        a = list_of_integers[mid]
        b = list_of_integers[mid + 1]

        if a < b:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]
