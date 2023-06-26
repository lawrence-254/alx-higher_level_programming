#!/usr/bin/python3
import sys
def safe_function(fct, *args):
	'''
	a function that executes a function safely
	Returns the result of the function
	Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
	'''
	try:
		result = fct(*args)
		return (result)
	except:
		print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
		return (None)
