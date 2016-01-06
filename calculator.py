"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def tokenize(input):
    """Parses space delineated input string and returns list of tokens."""

    tokens = input.split(' ')
    return tokens


# Your code goes here
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read


# tokenize("+ 0 1")
# tokenize("mod 10 3")

