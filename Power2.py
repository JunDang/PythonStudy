def interPower (base, exp):
	result = 1
	exp = abs(exp)
	for i in range(exp):
		result = result * base
	return result
print interPower(2, 3)