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
    word = secret_word;
    for letter in letters_guessed:
        while letter in word:
            word = word[0:word.index(letter)]+word[word.index(letter)+1:]
    #print(word);
    if word == "":
        return True;
    else:
        return False;
#print(is_word_guessed("apple", ['e','i','k','p','r', 's']));



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = secret_word;
    wordArray = ["_ "]*len(secret_word);
    for letter in letters_guessed:
        while letter in word:
            wordArray[word.index(letter)] = letter;
            word = word[0:word.index(letter)]+"_"+word[word.index(letter)+1:]
    printed = "";
    for i in range(len(secret_word)):
        printed += wordArray[i];
    print(printed);
    return printed;
#get_guessed_word("apple", ['e','i','k','p','r', 's']);



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase;
    for letter in letters_guessed:
        #print("HERE",alphabet.index(letter));
        alphabet = alphabet[0:alphabet.index(letter)]+alphabet[alphabet.index(letter)+1:]
    return alphabet;
#print(get_available_letters(['e','i','k','p','r', 's']));

def get_unique_letters(secret_word):
    word = secret_word;
    counter = 0;
    for letter in word:
        #print(word,"-",letter);
        if letter in word:
            counter += 1;
        while letter in word:
            word = word[0:word.index(letter)]+word[word.index(letter)+1:];
        #print(counter);
    return counter;

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
    tries = 6;
    warnings = 3;
    letters_guessed = [];
    unique = get_unique_letters("tact");
    #print("unique",unique);
    print("Welcome to the game Hangman!");
    print("I am thinking of a word that is", len(secret_word), "letters long.");
    print("You have", warnings, "warnings left.");
    #print("Available letters:", string.ascii_lowercase);
    while tries > 0:
        print("-----------------");
        print("You have", tries, "guesses left.");
        print("Available letters:", get_available_letters(letters_guessed));
        guess = input("Please guess a letter: ");
        while len(guess) > 1:
            guess = input("Please enter one letter only: ");
        if guess in string.ascii_letters and guess not in letters_guessed:
            letters_guessed.append(guess.lower());
            if guess not in secret_word:
                if guess in "aeiou":
                    tries -= 2;
                else:
                    tries -= 1;
                print("Oops! That letter is not in my word:");
                get_guessed_word(secret_word, letters_guessed);
            else:
                print("Good guess:"); 
                get_guessed_word(secret_word, letters_guessed);
        else:
            if warnings > 0:
                warnings -= 1;
            else:
                tries -= 1;
            if guess not in string.ascii_letters:
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:");
            if guess in letters_guessed:
                print("Oops! You have already entered that letter. You have", warnings, "warnings left: ");
            get_guessed_word(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is:", tries*unique);
            return;
    print("-----------------");
    print("Sorry, you ran out of guesses. The word is:", secret_word);
    pass;



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #print(my_word.count(" "));
    #print(other_word.count(" "))
    if len(my_word)-my_word.count(" ") != len(other_word):
        return False;
    my = [];
    other = [];
    for letter in my_word:
        if letter != " ":
            my.append(letter);
    for letter in other_word:
        other.append(letter);
    for i in range(len(my)):
        if my[i] in string.ascii_letters:
            if my[i] != other[i]:
                return False;
    return True;
#print(match_with_gaps("te_ t", "tact"));
#print(match_with_gaps("a_ _ le", "banana"));
#print(match_with_gaps("a_ _ le", "apple"));
#print(match_with_gaps("a_ ple", "apple"));
#print(match_with_gaps("a_ pl_ ", "apple"));
#print(match_with_gaps("a_ plb", "apple"));



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    words = "";
    for word in wordlist:
        #print(word);
        if match_with_gaps(my_word, word):
            words += word + " ";
    if words == "":
        print("No matches found");
    else:
        print(words);
#show_possible_matches("t_ _ t")
#show_possible_matches("abbbb_ ")
#show_possible_matches("a_ pl_ ")


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
    tries = 6;
    warnings = 3;
    letters_guessed = [];
    unique = get_unique_letters(secret_word);
    #print("unique",unique);
    print("Welcome to the game Hangman!");
    print("I am thinking of a word that is", len(secret_word), "letters long.");
    print("You have", warnings, "warnings left.");
    #print("Available letters:", string.ascii_lowercase);
    while tries > 0:
        print("-----------------");
        print("You have", tries, "guesses left.");
        print("Available letters:", get_available_letters(letters_guessed));
        guess = input("Please guess a letter: ");
        while len(guess) > 1:
            guess = input("Please enter one letter only: ");
        if guess in string.ascii_letters and guess not in letters_guessed:
            letters_guessed.append(guess.lower());
            if guess not in secret_word:
                if guess in "aeiou":
                    tries -= 2;
                else:
                    tries -= 1;
                print("Oops! That letter is not in my word:");
                get_guessed_word(secret_word, letters_guessed);
            else:
                print("Good guess:"); 
                get_guessed_word(secret_word, letters_guessed);
        elif guess == "*":
            print("Possible word matches are:");
            show_possible_matches(get_guessed_word(secret_word, letters_guessed));
        else:
            if warnings > 0:
                warnings -= 1;
            else:
                tries -= 1;
            if guess not in string.ascii_letters:
                print("Oops! That is not a valid letter. You have", warnings, "warnings left:");
            if guess in letters_guessed:
                print("Oops! You have already entered that letter. You have", warnings, "warnings left: ");
            get_guessed_word(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is:", tries*unique);
            return;
    print("-----------------");
    print("Sorry, you ran out of guesses. The word is:", secret_word);
    pass;
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
