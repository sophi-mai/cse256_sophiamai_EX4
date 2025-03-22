PHASE 1 VERSION 1 FILE: 
#1 GUESS THE WORD GAME: 
a. list_to_str: selects a word from a list using a randomized index #
    ; __current_word = list_to_str(listin)
b. run_word(word): reveals each letter of a word as it is guessed. Returns "FailedGuess" if any of the letters in the word are guessed incorrectly 
    ; run_word_output = run_word(current_word)
c. run_t(word_itr): ACCEPTS "FailedGuess", returns "Rerun" 
d. rerun(inbound): ACCEPTS "Rerun", prints "Reset Variable: current_word" 

#2 PYTEST
None


PHASE 2 VERSION 1 FILES 
#1 GUESS THE WORD GAME:
a. list_to_str: selects a word from a list with a random index 
b. run_word: returns the word and the length of the word, if the user's first guess is correct (second letter)
c. run_word2: returns the fourth letter if the third letter is guessed correctly. Returns a congratulatory message if there are only 3 letters in the word. 
d. run_word3: TBA 
    i. the fourth letter, the word, and the length of the word (in a separate branch)

#2 PYTEST FILE:
a. Checking if the game selects a word from the correct list.
b. Checking if guesses are processed correctly (correct vs. incorrect guesses)
