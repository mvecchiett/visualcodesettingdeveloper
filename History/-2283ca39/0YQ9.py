#coding: utf-8 -*.

def a_function(x):
	result = 0
	if x > 0 and x < 5:
		result = x ** 2
	elif x >= 5 and x < 10:
		pass
	else:
		result = (x ** 4) +1
	return result

a_function(2)

a_function(7)

a_function(12)