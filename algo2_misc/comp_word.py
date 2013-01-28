# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

import re

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    out_word = ''
    if re.match(r'[A-Z]+',word) != None:
        if re.match(r'[A-Z]+',word).group(0) == word:
            for i in range(len(word)):
                out_word = out_word + '+' + word[::-1][i] + '*' + str(10**i)
                return out_word[1:]
    return word

        
print compile_word('YOU')
print compile_word('+')
print compile_word('A+')