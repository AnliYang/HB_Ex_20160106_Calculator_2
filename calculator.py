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

def calculate(tokens):
    """Chooses and calls arithmetic function indicated by first token."""

    # Convert to ints
    calc_ints = []
    for num in tokens[1:]:
        calc_ints.append(float(num))

    if tokens[0] == "+":
        # print add(calc_ints[0], calc_ints[1])
        print reduce(add, calc_ints)        

    elif tokens[0] == "-":
        print subtract(calc_ints[0], calc_ints[1])

    elif tokens[0] == "*":
        print multiply(calc_ints[0], calc_ints[1])

    elif tokens[0] == "/":
        print divide(calc_ints[0], calc_ints[1])

    elif tokens[0] == "square":
        print square(calc_ints[0])

    elif tokens[0] == "cube":
        print cube(calc_ints[0])

    elif tokens[0] == "pow":
        print power(calc_ints[0], calc_ints[1])

    elif tokens[0] == "mod":
        print mod(calc_ints[0], calc_ints[1])

    else: 
        print "I don't understand!"


while True:
    calc_input = raw_input("> ")

    calc_tokens = tokenize(calc_input)
    
    if calc_tokens[0] == 'q':
        break
    else:
        calculate(calc_tokens)


