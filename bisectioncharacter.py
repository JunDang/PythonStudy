def isIn(char, aStr):
	if aStr == '':
		return False
	if len(aStr) == 1
		return char == aStr
	midIndex = len(aStr)/2
	midchar = aStr[midIndex]
	if midchar == char:
		return True
	elif midchar > char:
		return isIn(char, aStr[:midIndex])
	else:
		return isIn(char, aStr[midIndex+1:])
		