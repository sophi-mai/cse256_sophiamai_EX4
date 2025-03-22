# Sophia Mai
# CI256 Spring 2025
# EX 4: Write a Python script named guess_the_word.py that implements the following:
# The program selects a random word from a predefined list.
# The user guesses one letter at a time.
# If the guessed letter is in the word, it is revealed; otherwise, the program indicates the guess is incorrect.
# TODO: The game continues until the user correctly guesses the entire word or runs out of attempts.
# Display a congratulatory message when the word is guessed.


from random import randint
wordlist = ['pig', 'cow', 'cat', 'dog', 'monkey', 'zebra', 'fish', 'bird']

def list_to_str(listin):
    randindx = randint(0,7)
    to_str = [x for x in wordlist[randindx]]
    return to_str

def run_word(word, x): # x signifies the first guess
    lenword = len(word)
    # print(word[0])
    # x = input("Guess the next letter: ")
    if x == word[1]:
        return word, lenword
    else:
        return "Oh no!"

def run_word2(runword):
    # a) print(word[0:2])
    # b) x = input("Guess the next letter: ")
    word, length = runword
    x = word[2]  # (a, b), the second guess was correct
    if length == 3:
        return ("Nice!")
    else:
        y = word[3] #return the next letter
        if x == word[2]:
            return y, word
        else:
            return "Oh no! That's not right... let's try again"

# run_word2(run_word(list_to_str(wordlist))) -->

def run_word3(x, word, y):
    z = ( word.index(y) + 1 )
    if x == word[z]:
        # return "Nice!"
        return z
    else:
        return "Oh no! That's not right... let's try again"
