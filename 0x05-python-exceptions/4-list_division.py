#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	'''
	a function that divides element by element 2 lists.
	Returns a new list (length = list_length) with all divisions
	'''
	result = []
	try:
		for i in range(0, list_length):
			try:
				division_result = my_list_1[i]/my_list_2[i]
				result.append(division_result)
			except ZeroDivisionError:
				print("division by 0")
				result.append(0)
			except (TypeError, ValueError):
				print("wrong type")
				result.append(0)
			except IndexError:
				print("out of range")
				result.append(0)
	finally:
		return (result)
