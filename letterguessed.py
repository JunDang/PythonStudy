def isWordGuessed(secretWord, lettersGuessed):
    #secretWord: string, the word the user is guessing
    #lettersGuessed: list, what letters have been guessed so far
    #returns: boolean, True if all the letters of secretWord are in lettersGuessed;
     # False otherwise
	for letter in secretWord.lower():
		if not (letter in lettersGuessed):
			return False
	return True
secretWord = 'apple'
lettersGuessed = ['a', 'p', 'p', 'l', 'e', 's']
print isWordGuessed(secretWord, lettersGuessed)		