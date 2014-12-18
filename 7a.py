# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
   # Returns a list of valid words. Words are strings of lowercase letters.
    
   # Depending on the size of the word list, this function may
    #take a while to finish.
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    #wordlist (list): list of words (strings)

    #Returns a word from wordlist at random
  
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    #secretWord: string, the word the user is guessing
   # lettersGuessed: list, what letters have been guessed so far
   # returns: boolean, True if all the letters of secretWord are in lettersGuessed;
     # False otherwise
      
    # secretWord = 'apple' 
    #lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    #print isWordGuessed(secretWord, lettersGuessed)
    #False
  
    # FILL IN YOUR CODE HERE...
    i = 0
    for letter in secretWord:
        if letter not in lettersGuessed:
            i += 1
    return not (i > 0)


def getGuessedWord(secretWord, lettersGuessed):
    #secretWord: string, the word the user is guessing
    #lettersGuessed: list, what letters have been guessed so far
    #returns: string, comprised of letters and underscores that represents
    #what letters in secretWord have been guessed so far.
    # FILL IN YOUR CODE HERE...

    wordGuessed = ''

    for letter in secretWord:
        if letter in lettersGuessed:
            wordGuessed = wordGuessed + secretWord[secretWord.index(letter)]
        else:
            wordGuessed = wordGuessed + '_ '

    return wordGuessed


def getAvailableLetters(lettersGuessed):
    #lettersGuessed: list, what letters have been guessed so far
    #returns: string, comprised of letters that represents what letters have not
    #yet been guessed.
    # FILL IN YOUR CODE HERE...

    alphabet = string.ascii_lowercase
    alphalist = []

    # create a list of the alphabet
    for letter in alphabet:
        alphalist.append(letter)

    # remove lettersGuessed from alphalist
    for letter in lettersGuessed:
        if letter in alphalist:
            alphalist.remove(letter)

    # convert alphalist into a string
    #global lettersRemaining
    lettersRemaining = ''
    for letter in alphalist:
        lettersRemaining += letter

    return lettersRemaining
            

def hangman(secretWord):
    #'''
    #secretWord: string, the secret word to guess.

    #Starts up an interactive game of Hangman.

    #* At the start of the game, let the user know how many 
    #  letters the secretWord contains.

    #* Ask the user to supply one guess (i.e. letter) per round.

    #* The user should receive feedback immediately after each guess 
   #   about whether their guess appears in the computers word.

   # * After each round, you should also display to the user the 
   #   partially guessed word so far, as well as letters that the 
   #   user has not yet guessed.

    #Follows the other limitations detailed in the problem write-up.
    # FILL IN YOUR CODE HERE...
	#loadWords()
	print 'Welcome to the game, Hangman!'
	print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
	guesses = 8
	#print 'You have ' + str(guesses)+ ' guesses left.'--wrong place
	#print 'Available letters: abcdefghijklmnopqrstuvwxyz'---wrong
	lettersGuessed = []
	#print 'Available letters: ' + getAvailableLetters(lettersGuessed)---wrong place
	while guesses > 0:
		print '-----------'
		print 'You have ' + str(guesses)+ ' guesses left.'
		print 'Available letters: ' + getAvailableLetters(lettersGuessed)
		wordGuessed = raw_input('Please guess a letter: ')
		if wordGuessed in secretWord:
			if wordGuessed in lettersGuessed:
				print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
			else: 
				lettersGuessed.append(wordGuessed)
				print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
				if isWordGuessed(secretWord, lettersGuessed):
					#print 'Congratulations, you won!' --it is at the wrong place
					break
				#else:
				#	print 'You have ' + str(guesses) +' guesses left.' ---wrong place
				#	print 'Available letters: ' + getAvailableLetters(lettersGuessed)----wrong place
			
		else: 
			print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
			guesses = guesses - 1
		#lettersGuessed.append(wordGuessed)---wrong place
	print '-----------'
	if guesses == 0:
		#print '-----------'
		print 'Sorry, you ran out of guesses. The word was else.'
	else: 
		#print '-----------'
		print 'Congratulations, you won!'
	





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord = 'tact'
#hangman(secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
