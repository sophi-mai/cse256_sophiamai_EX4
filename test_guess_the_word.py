# Sophia Mai
# CIS 256 Spring 2025
# EX 4 - testing

import pytest
from guess_the_word import *

def test_l2s():
    assert ''.join(list_to_str(wordlist)) in wordlist

def test_theguess():
    pass
    # run_word('local')
