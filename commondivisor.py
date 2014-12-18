def gcdIter(a, b):
	test = min(a, b)
	while a % test != 0 or b % test != 0:
		test = test - 1
	return test	
print gcdIter(2, 12)