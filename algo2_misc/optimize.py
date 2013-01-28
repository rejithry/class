# Do Not Repeat Repeated Work
#
# Focus: Units 5 and 6: Interpreting and Optimization
#
#
# In class we studied many approaches to optimizing away redundant
# computation. For example, "X * 0" can be replaced with "0", because we
# know in advance that the result will always be 0. However, even if we do
# not know the answer in advance, we can sometimes save work. Consider this
# program fragment:
#
#       x = a + b + c;
#       y = 2;
#       z = a + b + c; 
#
# Even though we do not know what "a + b + c" will be, there is no reason
# for us to compute it twice! We can replace the program with: 
#
#       x = a + b + c;
#       y = 2;
#       z = x;          # works since "x = a + b + c;" above
#                       # and neither a nor b nor c has been changed since
#
# ... and always compute the same answer. This family of optimizations is
# sometimes called "common expression elimination" -- the subexpression
# "a+b+c" was common to two places in the code, so we eliminated it in one. 
#
# In this problem we will only consider a special case of this
# optimization. If we see the assignment statement:
#
#       var1 = right_hand_side ;  
#
# Then all subsequent assignment statements:
#
#       var2 = right_hand_side ;
#
# can be replaced with "var2 = var1 ;" provided that the "right_hand_side"s
# match exactly and provided that none of the variables involved in
# "right_hand_Side" have changed. For example, this program cannot be
# optimized in this way:  
#
#       x = a + b + c;
#       b = 2;
#       z = a + b + c; 
#
# Even though the right-hand-sides are exact matches, the value of b has
# changed in the interim so, to be safe, we have to recompute "a + b + c" and
# cannot replace "z = a + b + c" with "z = x". 
#
# For this problem we will use the abstract syntax tree format from our
# JavaScript interpreter. Your procedure will be given a list of statements
# and should return an optimized list of statements (using the optimization
# above). However, you will *only* be given statement of the form:
#
#       ("assign", variable_name, rhs_expression) 
#
# No other types of statements (e.g., "if-then" statements) will be passed
# to your procedure. Similarly, the rhs_expression will *only* contain
# expressions of these three (nested) form:
#
#       ("binop", exp, operator, exp)
#       ("number", number)
#       ("identifier", variable_name) 
#
# No other types of expressions (e.g., function calls) will appear. 
#
# Write a procedure "optimize()" that takes a list of statements (again,
# only assignment statements) as input and returns a new list of optimized
# statements that compute the same value but avoid recomputing
# whole right-hand-side expressions. (If there are multiple equivalent
# optimizations, return whichever you like.) 
#
# Hint: x = y + z makes anything involving y and z un-available, and
# then makes y + z available (and stored in variable x).   

def optimize(ast):
    op_ast = ast[:]
    for stmt_num in range(0,len(ast)):
        var_list = []
        stmt = ast[stmt_num]
        var_list = get_var_list(stmt[2])
        #print  var_list   
        for i in range(stmt_num + 1, len(ast)):
            n_stmt = ast[i]
            if n_stmt[1] in var_list and not(n_stmt[2][0] == 'identifier' and n_stmt[2][1] == n_stmt[1]) :
                break;
            if n_stmt[2] ==  stmt[2]:
                op_ast[i] = (op_ast[i][0],op_ast[i][1],('identifier',stmt[1]))
    return op_ast

def get_var_list(stmt):
        if stmt[0] == 'identifier':
            return [stmt[1]]
        elif stmt[0] == 'binop':
            return get_var_list(stmt[1]) + get_var_list(stmt[3])
        else:
            return []
# We have included some testing code to help you check your work. Since
# this is the final exam, you will definitely want to add your own tests.

example1 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("number", 2)) ,
("assign", "z", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
] 
answer1 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("number", 2)) ,
("assign", "z", ("identifier", "x")) ,
] 
         
print (optimize(example1)) == answer1


example2 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "a", ("number", 2)) ,
("assign", "z", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
] 

print (optimize(example2)) == example2

example3 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "x", ("number", 2)) ,
("assign", "z", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
] 
answer3 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("identifier", "x")) ,
("assign", "x", ("number", 2)) ,
("assign", "z", ("identifier", "y")) , # cannot be "= x" 
] 

print (optimize(example3)) == answer3

example4 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "z", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
("assign", "b", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
("assign", "z", ("number", 5)) ,
("assign", "p", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "q", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "r", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
] 

answer4 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "z", ("binop", ("identifier","c"), "+", ("identifier","d"))) ,
("assign", "b", ("identifier", "z")) ,
("assign", "z", ("number", 5)) ,
("assign", "p", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "q", ("binop", ("identifier","b"), "+", ("identifier","c"))) ,
("assign", "r", ("identifier", "b")) ,
] 

print optimize(example4) == answer4

example4 = [ 
    ('assign', 'x', ('binop', ('identifier', 'a'), '+', ('identifier', 'b'))),
    ('assign', 'a', ('identifier', 'a')),
    ('assign', 'y', ('binop', ('identifier', 'a'), '+', ('identifier', 'b'))),
]

answer4 = [ 
    ('assign', 'x', ('binop', ('identifier', 'a'), '+', ('identifier', 'b'))),
    ('assign', 'a', ('identifier', 'a')),
    ('assign', 'y', ('identifier', 'x')),
]

print optimize(example4) == answer4

example1 = [('assign', 'x', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
('assign', 'y', ("number", 2)), 
('assign', 'z', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'b')), '+', ('identifier', 'c')))]

answer1 = [('assign', 'x', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
('assign', 'y', ("number", 2)), 
('assign', 'z', ('identifier', 'x'))]
print optimize(example1) == answer1

#       x = a + e + b + c;
#       e = 2;
#       z = a + e + b + c; 
#

example2 = [('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
('assign', 'e', ("number", 2)), 
('assign', 'z', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c')))]

answer2 = [('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))), 
('assign', 'e', ("number", 2)), 
('assign', 'z', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c')))]

print optimize(example2) == answer2


example4a = [\
    ("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
    ("assign", "y", ("binop", ("identifier","x"), "+", ("identifier","c"))) ,
    ("assign", "z", ("binop", ("binop", ("identifier","a"), "+", ("identifier","b")), "+", ("identifier","c"))) ,
]
answer4a = [\
    ("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
    ("assign", "y", ("binop", ("identifier","x"), "+", ("identifier","c"))) ,
    ("assign", "z", ("identifier", "y")) ,
]

print optimize(example4a) == answer4a
print optimize(example4a)

#       x = a + e + b + c;
#       e = 2;
#       z = a + e + b + c;
#

example4b = [ \
    ('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))),
    ('assign', 'e', ("number", 2)),
    ('assign', 'z', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))),
]

answer4b = [ \
    ('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))),
    ('assign', 'e', ("number", 2)),
    ('assign', 'z', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c')))
]

print optimize(example4b) == answer4b

#       x = a + e + b + c;
#       y = e;
#       z = a + e + b + c;
#

example4c = [ \
    ('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))),
    ('assign', 'y', ("identifier", 'e')),
    ('assign', 'z', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))),
]

answer4c = [ \
    ('assign', 'x', ('binop', ('binop', ('binop', ('identifier', 'a'), '+', ('identifier', 'e')), '+', ('identifier', 'b')), '+', ('identifier', 'c'))),
    ('assign', 'y', ("identifier", 'e')),
    ('assign', 'z', ("identifier", 'x'))
]

print optimize(example4c) == answer4c

example5 = [\
   ("assign", "a", ("identifier", "b")) ,
   ("assign", "a", ("identifier", "a")) ,
]

#Some people might believe that a = a should be optimized away. Well, it should practically. But
#this is not allowed under the rules given in the assignment. a = a is not a "subsequent" assignment
#statement for 'a'.
answer5 = [\
    ("assign", "a", ("identifier", "b")) ,
    ("assign", "a", ("identifier", "a")) ,
]

print optimize(example5) == answer5


#       self-assign
#       x = x + z + 1;
#       y = x + z + 1;
example6 = [\
    ("assign", "x", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1")))),
    ("assign", "y", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1"))))
]

# Some people might think that y = x would be a correct optimization, and I think they would be technically right.
# But I have seen people say this shouldn't be optimized. I would appreciate help with reasoning here.
answer6 =  [\
    ("assign", "x", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1")))),
    ("assign", "y", ("binop", ("identifier","x"), "+", ("binop", ("identifier","z"), "+", ("number","1"))))
]

print optimize(example6) == answer6

print optimize(example6)

example7 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("number", 2)) ,
("assign", "d", ("number", 2)) ,
("assign", "z", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
]

# This one is a still in debate to me. Some people say that d = 2 is replaced with d = y. And that is what I have put
# in the answer below. However, I still am not 100% convinced that this should be the case.
# 7-6 states:
#
# If we see the assignment statement:
#
#       var1 = right_hand_side ;
#
# Then all subsequent assignment statements:
#
#       var2 = right_hand_side ;
#
# can be replaced with "var2 = var1 ;" provided that the "right_hand_side"s
# match exactly and provided that none of the variables involved in
# "right_hand_Side" have changed.
#
# Notice the key phrase --- "provided that none of the VARIABLES involved in "right_hand_Side" have changed.". And certainly, the constant number 2 IS NOT a variable.
# I would appreciate official reasoning and/or response on this one.
answer7 = [ \
("assign", "x", ("binop", ("identifier","a"), "+", ("identifier","b"))) ,
("assign", "y", ("number", 2)) ,
("assign", "d", ("identifier", "y")) ,
("assign", "z", ("identifier", "x")) ,
]

print optimize(example7) == answer7