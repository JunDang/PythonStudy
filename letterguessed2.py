def getGuessedWord(secretWord, lettersGuessed):
	result = ''
	for letter in secretWord:
		if not (letter in lettersGuessed):
			result = result + ' - '
		else:
			result = result + str(letter)
	return result
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)