def AlphaSubstrings(s):
	s = s.lower()
	i = 0
	longest = ''
	for j in range(1, len(s)):
		if s[j] < s[j-1]:
			if len(longest) < j - i: # j - i is the length of curstring
				longest = s[i: j]  # curstring
			i = j
	return longest
print AlphaSubstrings('azcbobobegghakl')
