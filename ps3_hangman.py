# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    input_list = list(secretWord)
    result = []
    for i in range(len(input_list)):
        if input_list[i] in lettersGuessed:
            result.append(input_list[i])
    if len(result) == len(input_list):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    input_list = list(secretWord)
    result = []
    x = ""
    for i in range(len(input_list)):
        if input_list[i] in lettersGuessed:
            result.append(input_list[i])
        else:
            result.append("_ ")
    return x.join(result)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_list = list(alphabet)
    string_result = ""
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in input_list:
            input_list.remove(lettersGuessed[i])
    return string_result.join(input_list)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    total_no_of_guess = 8
    input_str = ""
    lettersGuessed = []

    while total_no_of_guess >= 1:
      if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break

      print("-------------")
      print("You have", total_no_of_guess, "guesses left")

      print("Available letters:", getAvailableLetters(lettersGuessed) )
      input_str = input("Please guess a letter: ")
      input_str_list = list(input_str)
      lettersGuessed = lettersGuessed + input_str_list
      if input_str in secretWord and input_str not in lettersGuessed:
        print(lettersGuessed)
        gussed_output = getGuessedWord(secretWord, lettersGuessed)
        print("Good guess", gussed_output)
      elif input_str in lettersGuessed:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
      elif input_str not in secretWord:
        print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        total_no_of_guess -= 1
    
     

print("Welcome to the game Hangman!")
print(hangman("tact"))






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
