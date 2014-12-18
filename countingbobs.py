def CountingBobs(s):
	s = s.lower()
	numBobs = 0
	for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
	print 'Number of times bob occurs is:', numBobs
print CountingBobs('azcbobobegghakl')
