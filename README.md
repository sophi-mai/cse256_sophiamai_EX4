<b>PHASE 1 VERSION 1 FILE:</b><br>
#1 GUESS THE WORD GAME: <br>
a. list_to_str: selects a word from a list using a randomized index # <br>
    ; __current_word = list_to_str(listin) <br>
b. run_word(word): reveals each letter of a word as it is guessed. Returns "FailedGuess" if any of the letters in the word are guessed incorrectly <br>
    ; run_word_output = run_word(current_word) <br>
c. run_t(word_itr): ACCEPTS "FailedGuess", returns "Rerun" <br>
d. rerun(inbound): ACCEPTS "Rerun", prints "Reset Variable: current_word" <p>
</p>
#2 PYTEST <br>
None
<p>

<b>PHASE 2 VERSION 1 FILES</b><br>
<i>#1 GUESS THE WORD GAME:</i><br>
a. list_to_str: selects a word from a list with a random index <br>
b. run_word: returns the word and the length of the word, if the user's first guess is correct (second letter) <br>
c. run_word2: returns the fourth letter if the third letter is guessed correctly. Returns a congratulatory message if there are only 3 letters in the word.<br>
d. run_word3: TBA <br>
    <ol>i. the fourth letter, the word, and the length of the word (in a separate branch)<br></ol>
<p>
<i>#2 PYTEST FILE:</i><br>
a. Checking if the game selects a word from the correct list.<br>
b. Checking if guesses are processed correctly (correct vs. incorrect guesses)
