def twoPower():
	result = 0
	num = 0
	while True:
		num = num + 1
		result = 2**num
		yield result
twoP = twoPower()
print twoP.next()
print twoP.next()
print twoP.next()
print twoP.next()
print twoP.next()
print twoP.next()
		