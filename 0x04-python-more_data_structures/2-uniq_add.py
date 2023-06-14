#!/usr/bin/python3
def uniq_add(my_list=[]):
	u_list = set(my_list)
	n = 0

	for i in u_list:
		n += i
	
	return n
