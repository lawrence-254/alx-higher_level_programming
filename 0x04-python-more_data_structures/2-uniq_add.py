#!/usr/bin/python3
def uniq_add(my_list=[]):
	li = set(my_list)
	n = 0
	
	for i in li:
		n += i
	return (n)
