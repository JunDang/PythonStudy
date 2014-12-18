import string
allLetters = string.ascii_lowercase
def getAvailableLetters(lettersGuessed):
	result = ''
	for letter in allLetters:
		if not (letter in lettersGuessed):
			result = result + str(letter)
	return result
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)