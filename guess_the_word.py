# Sophia Mai
# CI256 Spring 2025
# EX 4: Write a Python script named guess_the_word.py that implements the following:
# The program selects a random word from a predefined list.
# The user guesses one letter at a time.
# If the guessed letter is in the word, it is revealed; otherwise, the program indicates the guess is incorrect.
# The game continues until the user correctly guesses the entire word or runs out of attempts.
# Display a congratulatory message when the word is guessed.


from random import randint
wordlist = ['pig', 'cow', 'cat', 'dog', 'monkey', 'zebra', 'fish', 'bird']

def list_to_str(listin):
    randindx = randint(0,7)
    to_str = [x for x in wordlist[randindx]]
    return to_str

current_word = list_to_str(wordlist)

def run_word(word):
    print(word[0])
    x = input("Guess the next letter: ")
    if x == word[1]:
        print(''.join(word[0:2]))
        for each in word[2:]:
            a = input("Guess the next letter: ")
            if a == each:
                print(''.join(word[0:(word.index(each)+1)]))
                continue
            else:
                print("Oh no! That's not right.. try again")
                return "FailedGuess"
        return "Nice!"
    else:
        print("Oh no! That's not right.. try again")
        return "FailedGuess"

run_word_output = run_word(current_word)

def run_t(word_itr):
    if word_itr == "FailedGuess":
        return "Rerun"
    else:
        return "Nice!"

# run_t(run_word_output)

def rerun(inbound):
    if inbound == "Rerun":
        print("Reset Variable: current_word")
    else:
        print("Nice! You guessed the word!")

rerun(run_t(run_word_output))