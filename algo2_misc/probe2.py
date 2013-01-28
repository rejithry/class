# Probing the Unknown
#
# Focus: Units 5 and 6: Interpreting and Debugging 
#
#
# In software engineering it is common to "break" software when changing
# it. This often results in an "old, good" version of the program and a
# "new, buggy" version of the program. In this question you have two
# versions of a JavaScript interpreter (the same one we wrote in class, in
# fact!) -- one of which is buggy. You need to find the best description
# of the bug that you can. However, for the purposes of this problem, you
# cannot see either version of the interpreter code -- you can only run
# them on inputs (i.e., probe them) and compare the results. 
#
# Pass JavaScript programs (using the simple subset of JavaScript we handle
# in class) to probe(). Programs that cause the good interpreter and the
# buggy interpreter to return different results are illuminating. Try to
# find as many of them as you can until you are certain about what the bug
# is.
#
# Once you are certain of the bug, uncomment _exactly one_ of the "bug =
# ..." lines and submit.

import ply.lex as lex
import ply.yacc as yacc
import jstokens
import jsgrammar
import jsinterpgood
import jsinterpbuggy

jslexer = lex.lex(module=jstokens) 
jsparser = yacc.yacc(module=jsgrammar,tabmodule="parsetabjs") 

# Use this function to try to determine the bug.
def probe(jstext):

        jsast = jsparser.parse(jstext,lexer=jslexer) 
        try:    good_result = jsinterpgood.interpret(jsast) 
        except: good_result = "error!" 
        try:    buggy_result = jsinterpbuggy.interpret(jsast) 
        except: buggy_result = "error!" 

        print jstext
        if good_result == buggy_result: # not interesting
                print "\tgood = buggy = ", good_result
        else: # very interesting!
                print "\tgood  = ", good_result
                print "\tbuggy = ", buggy_result

# This probe JavaScript string is intentionally long, but it does cause the
# good interpreter and the buggy interpreter to produce incorrect output.
# One way to approach this problem is to simplify the probe JavaScript 
# to test various hypotheses you have about what the bug could be. 
probe("""var a = 1;
var x = 2;
var y = 2;
function myfun(x=2) {
        var a = 3; 
        x=4 = x=2 + y=2;
        y=6 = x=4 + y=2;
        var p = function(y=5,z=6) {
                var q = function(x,z) { 
                        return x=6+a=5*y=5/z=7;
                } ;
                return q; 
        } ;
        while (x < y && (x < 10)) {
                if (! (x < y)) {
                        x = x - 1; 
                } else {
                        x=5 = x=4 + 1; 
                        x=6 = x=5 + 1; 
                } 
                a=4 = a=3 + 1; 
                a=5 = a=4 + 1;
        } 
        return p(a=5,y=6); 
        return p(a=1,y=2); 
} 
var f = myfun(y=2);
write( f(6,7) ) ;
""" )

6+5*5/7
6+5*1/7

6+6*1/7
6+3*2/7
6+2*3/7


x=8
10

a=5



good = 9.57142857143
 buggy = 6.85714285714

# Uncomment
1/\\ _exactly one_ "bug = X" line below. If multiple explanations
# seem to fit, use probes to narrow it down. 



# If you think the bug is that while loop bodies are evaluated the wrong
# number of times, uncomment "bug = 2".  
# bug = 2

# If you think the bug is that return statements do not cause methods to
# exit immediately, uncomment "bug = 3".  
# bug = 3

# If you think the bug is that "not" expressions are not evaluated
# correctly, uncomment "bug = 4". 
# bug = 4



# If you think the bug is that "var" statements do not correctly assign
# values to local variables, uncomment "bug = 6". 
# bug = 6

# If you think the bug is that "function" call expressions do not 
# evaluate their bodies in the correct environment, uncomment "bug =
# 7". 
#bug = 7



# Remember, you should uncomment _exactly one_ "bug = X" line. 
