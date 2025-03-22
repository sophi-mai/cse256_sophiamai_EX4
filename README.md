<b>Version 1 PHASE 1 FILE:</b><br>
<i>#1 GUESS THE WORD GAME:</i><br>
a. list_to_str: selects a word from a list using a randomized index # <br>
    ; __current_word = list_to_str(listin) <br>
b. run_word(word): reveals each letter of a word as it is guessed. Returns "FailedGuess" if any of the letters in the word are guessed incorrectly <br>
    <t>; run_word_output = run_word(current_word) <br>
c. run_t(word_itr): ACCEPTS "FailedGuess", returns "Rerun" <br>
d. rerun(inbound): ACCEPTS "Rerun", prints "Reset Variable: current_word"
<p>
</p>
<b>Version 1 PHASE 2 FILES</b><br>
<i>#1 GUESS THE WORD GAME:</i><br>
a. list_to_str: selects a word from a list with a random index <br>
b. run_word: returns the word and the length of the word, if the user's first guess is correct (second letter) <br>
c. run_word2: returns the fourth letter if the third letter is guessed correctly. Returns a congratulatory message if there are only 3 letters in the word.<br>
d. run_word3: TBA <br>
    <ol>i. the fourth letter, the word, and the length of the word (in a separate branch)<br></ol>
<p>
<i>#2 PYTEST FILE:</i><br>
a. Checks if the game selects a word from the correct list.<br>
b. Checks if guesses are processed correctly (correct vs. incorrect guesses)<br>

<hr></hr>

<b>Version 2 PHASE 1 FILE</b><br> 
<i>GUESS THE WORD GAME:</i><br> 
a. <i>@retry</i>: a global/decorator function. Handles incorrect guesses from by_letter(). <br>
b. <i>by_letter():</i> selects a word from the list, returns a congratulatory message if the whole word is guessed, sends a failed message to global/decorator if any letter is guessed incorrectly. <b><mark>(pushed remotely in repository "GitProject")</mark></b>

<b>Version 2 PHASE 2 FILES:</b><br> 
<i>The modifications have fixed the following issues:</i> <br> 
a. The program did not run continuously until a word was guessed. After two failed attempts the program would exit.<br>
b. The program did not properly handle correct guesses. A congratulatory message would only populate after two consecutive correct words. 
