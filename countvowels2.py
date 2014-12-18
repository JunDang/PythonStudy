def CountsVowel2(s):
	s = s.lower()
	return s.count('a' or 'e' or 'i' or 'o' or 'u')
print CountsVowel('azcbobobegghakl')
