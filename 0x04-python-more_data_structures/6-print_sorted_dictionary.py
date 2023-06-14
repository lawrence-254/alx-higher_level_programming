#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	list_ord = sorted(list(a_dictionary.keys()))
	for i in list_ord:
		print("{}: {}".format(i, a_dictionary.get(i)))
