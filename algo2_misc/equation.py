# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the 
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#
# Note that you will not be able to run your code yet since the 
# program is incomplete. Please SUBMIT to see if you are correct.

import string
import re 
import itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for translation in fill_in(formula):
        if valid(translation) :
            print  translation

    
def fill_in(formula):
        "Generate all possible fillings-in of letters in formula with digits."
        res = []
        digit_len =  len(set(re.findall(r'[A-Z]',formula)))
        letters = ''.join(set(re.findall(r'[A-Z]',formula)))
        for i in itertools.permutations(range(0,10),digit_len):
            table = string.maketrans(letters,''.join([str(j) for j in i]))
            res.append(formula.translate(table))
        return res
            
        

    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


print solve('XY**3 + Z**3 == XW**3 + X**3')
print solve('X**2 + Y**2 == Z**2')