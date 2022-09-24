# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if not(letter in letters_guessed):
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # guessed_word: string
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_ "
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = ""
    for letter in string.ascii_lowercase:
        if not(letter in letters_guessed):
            letters_not_guessed += letter
    return letters_not_guessed
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    word_is_guessed = False
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")
    
    # Loops until the user rounds out of guesses, breaks early if the word is solved
    while guesses_remaining > 0:
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        # Checks if the guess is a string. If not, it checks whether the remaining warnings or guesses needs to be decremented.
        if not(str.isalpha(guess)):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, " warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        # Checks if the guess was already guessed. If it was, it checks whether the remaining warnings or guesses needs to be decremented.
        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        # Checks to see if the guess is in the secret word and checks to see if the word is solved. If it is, the loop will break in the last if statement in this while loop.
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            word_is_guessed = is_word_guessed(secret_word, letters_guessed)
        else:
            letters_guessed.append(guess)
            if guess in "aeiou":
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        print("-------------")
        if word_is_guessed:
            break
    
    # Evaluates whether the user won or lost and prints appropriate message.
    if word_is_guessed:
        print("Congratulations, you won!")
        score = len(secret_word) * guesses_remaining
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)
            
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length, and none of the
        remaining letters have been guessed;
        False otherwise: 
    '''
    my_word_no_spaces = ""
    
    # Removes all spaces from my_word and stores it in my_word_no_spaces
    for c in my_word:
        if c != " ":
            my_word_no_spaces += c
            
    if len(my_word_no_spaces) != len(other_word):
        return False

    # Compares all characters to those in other_word. If the character is _, it makes sure the corresponding
    # letter in other_word hasn't been guessed already or it returns false
    i = 0
    for c in my_word_no_spaces:
        if c != "_":
            if c != other_word[i]:
                return False
        else:
            if other_word[i] in letters_guessed:
                return False
        i += 1

    return True
        


def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = ""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word, letters_guessed):
            matches += other_word + " "
    
    if len(matches) == 0:
        print("No matches found.")
    else:
        print(matches)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    word_is_guessed = False
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")
    
    # Loops until the user rounds out of guesses, breaks early if the word is solved
    while guesses_remaining > 0:
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed)
        # Checks if the guess is a string. If not, it checks whether the remaining warnings or guesses needs to be decremented.
        elif not(str.isalpha(guess)):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, " warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        # Checks if the guess was already guessed. If it was, it checks whether the remaining warnings or guesses needs to be decremented.
        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left: ", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        # Checks to see if the guess is in the secret word and checks to see if the word is solved. If it is, the loop will break in the last if statement in this while loop.
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            word_is_guessed = is_word_guessed(secret_word, letters_guessed)
        else:
            letters_guessed.append(guess)
            if guess in "aeiou":
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        print("-------------")
        if word_is_guessed:
            break
    
    # Evaluates whether the user won or lost and prints appropriate message.
    if word_is_guessed:
        print("Congratulations, you won!")
        score = len(secret_word) * guesses_remaining
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    