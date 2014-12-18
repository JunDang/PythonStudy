def maxLetter(s):
	s = s.lower()
	ST = s[0]
	for i in range(len(s)):
		if s[i] > ST:
			ST = s[i]		
	return ST
print maxLetter('dabci')
