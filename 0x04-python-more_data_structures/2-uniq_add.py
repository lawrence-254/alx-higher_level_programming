#!/usr/bin/python3
def uniq_add(my_list=[]):
	u_list = set(my_list)
	list_n = 0

	for i in u_list:
		list_n += i
	return list_n
