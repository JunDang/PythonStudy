def fourthPower(x):

	def square(x):
		result = 1
		for turn in range(2):
			#print('iteration: ' + str(turn) + ' current result: ' + str(result))
			result = result * x
		return result
	return square(square(x))
print fourthPower(3)
