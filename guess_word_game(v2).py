# Sophia Mai
# CIS256 Spring 2025
# EX 4

#1. GUESS THE WORD GAME
wordlist = ['pig', 'cow', 'horse', 'fish', 'bird', 'cat', 'dog', 'zebra', 'monkey']
from random import randint

def retry(func):
    def capture(*args):
        if func(*args) == "FAILED":
            pass
        result = func(*args)
        print("Nice! You guessed the word!") #None
        return result
    return capture()

@retry
def by_letter():
    randindx = randint(0,8)
    to_str = [x for x in wordlist[randindx]]
    last_letter = to_str[0]
    curr_letter = ''
    itr = 1 #oh no
    for each in to_str:
        curr_letter = each #nice!
        if itr == len(to_str):
            print(f'Nice! The word is {to_str}!')
            break
        elif curr_letter == to_str[0]:
            print(each)
            continue
        else:
            itr += 1
            x = input("Guess the next letter: ")
            if x == curr_letter:
                print(f'{to_str[0:itr]}')
                continue
            else:
                print("Oh no! That's incorrect, let's try again.")
                return "FAIL"
