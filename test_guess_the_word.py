# Sophia Mai
# CIS 256 Spring 2025
# EX 4 - testing

import pytest
from guess_the_word import *

def test_l2s():
    assert ''.join(list_to_str(wordlist)) in wordlist

def test_thefirstguess():
    assert run_word('pig', 'i') == ('pig', 3) # The first letter was guessed correctly; (Guess/Input == p)
def test_firstwrong():
    assert run_word('pig', 'o') == "Oh no!" # The guess was incorrect; (Guess/Input == o)

def test_followingguesses():
    assert run_word2(run_word('pig', 'i')) == "Nice!" # A three letter word was guessed correctly
    assert run_word2(run_word('horse', 'o')) == ('s', 'horse') # The second letter was guessed correctly, and run_word returns the next letter