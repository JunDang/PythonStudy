def evalQuadratic(a, b, c, x):
	result = 1
	for turn in range(2):
		#print('iteration: ' + str(turn) + ' current result: ' + str(result))
		result = result * x
		print result
	result2 = result*a
	print result2
	result3 = b*x
	print result3
	return result2 + result3 + c
print evalQuadratic(1, 1, 1, 2)